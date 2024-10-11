# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
"""Test that error message for not exist model have OS-depend delimiter in path"""
path = _get_export_dir("not_existing_dir")
pattern = os.path.sep + "{"
with self.assertRaises(IOError) as err:
    loader_impl.parse_saved_model(path)
self.assertTrue(pattern in str(err.exception))
