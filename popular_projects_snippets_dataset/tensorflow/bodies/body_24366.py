# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
bad_path = os.path.join(self.get_temp_dir(), "nonexistent.py")
with self.assertRaisesRegex(IOError,
                            "neither exists nor can be loaded.*par.*"):
    source_utils.load_source(bad_path)
