import os
import unittest
import tempfile
from PIL import Image
from ai_model import predict_crop_disease, validate_image
from werkzeug.security import generate_password_hash, check_password_hash

# NOTE: This test suite MUST NOT touch the real SQLite database in the repo.
# The project reads DATABASE_PATH from environment variables, so we override it
# and then import database.py only after setting the env var.


class _TestEnv:
    def __init__(self):
        self._tmp_dir = None
        self.db_path = None
        self._old_db_path = None

    def __enter__(self):
        self._tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self._tmp_dir.name, 'agriguard_test.db')
        self._old_db_path = os.environ.get('DATABASE_PATH')
        os.environ['DATABASE_PATH'] = self.db_path
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._old_db_path is None:
            os.environ.pop('DATABASE_PATH', None)
        else:
            os.environ['DATABASE_PATH'] = self._old_db_path
        self._tmp_dir.cleanup()


_test_env = _TestEnv()


class TestAgriGuard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        _test_env.__enter__()

        # Import after DB env is set (database.py reads env at import time)
        from database import init_db, get_db_connection

        cls._init_db = init_db
        cls._get_db_connection = staticmethod(get_db_connection)

        # Initialize isolated DB schema + seed diseases
        cls._init_db()

        # Create mock image/text artifacts under temp directory
        cls._artifacts_dir = tempfile.TemporaryDirectory()
        cls.test_image_path = os.path.join(cls._artifacts_dir.name, 'test_leaf_green.jpg')
        img = Image.new('RGB', (100, 100), color=(34, 139, 34))  # Forest Green
        img.save(cls.test_image_path)

        cls.test_invalid_path = os.path.join(cls._artifacts_dir.name, 'test_invalid.txt')
        with open(cls.test_invalid_path, 'w', encoding='utf-8') as f:
            f.write("This is not an image.")

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, '_artifacts_dir') and cls._artifacts_dir is not None:
            cls._artifacts_dir.cleanup()
        _test_env.__exit__(None, None, None)

    def test_database_tables(self):
        """Test database connection and verify all tables exist."""
        conn = self.__class__._get_db_connection()
        cursor = conn.cursor()

        tables = ['users', 'predictions', 'diseases', 'contacts', 'prediction_logs']
        for table in tables:
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (table,),
            )
            row = cursor.fetchone()
            self.assertIsNotNone(row, f"Table '{table}' does not exist in the database.")

        conn.close()

    def test_database_disease_seed(self):
        """Verify that crop disease seed records exist."""
        conn = self.__class__._get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM diseases")
        row = cursor.fetchone()
        self.assertEqual(row['count'], 12, "Fewer than 12 disease records exist in seed database.")
        conn.close()

    def test_password_hashing(self):
        """Verify password hashing utility integrity."""
        raw_pw = "farmer_password"
        hashed = generate_password_hash(raw_pw)
        self.assertNotEqual(raw_pw, hashed)
        self.assertTrue(check_password_hash(hashed, raw_pw))
        self.assertFalse(check_password_hash(hashed, "wrong_password"))

    def test_image_validation(self):
        """Test file uploads format check."""
        # Valid file
        try:
            validate_image(self.test_image_path)
        except Exception as e:
            self.fail(f"validate_image raised error on valid file: {e}")

        # Invalid extension
        with self.assertRaises(ValueError):
            validate_image(self.test_invalid_path)

        # File does not exist
        with self.assertRaises(FileNotFoundError):
            validate_image("non_existent_file.png")

    def test_prediction_pipeline(self):
        """Test leaf analysis classifier outputs a valid class and confidence."""
        disease, confidence = predict_crop_disease(self.test_image_path, selected_crop="Tomato")
        self.assertIn(
            disease,
            [
                "Tomato Early Blight",
                "Tomato Late Blight",
                "Tomato Healthy",
            ],
            f"Predicted disease '{disease}' is not within Tomato classes.",
        )
        self.assertGreaterEqual(confidence, 50.0)
        self.assertLessEqual(confidence, 100.0)

        print(f"\n[UNIT TEST] Test image prediction: {disease} ({confidence:.2f}% confidence)")


if __name__ == '__main__':
    unittest.main()

