# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
base_path = test.test_src_dir_path("/python/saved_model")
self.assertFalse(loader.maybe_saved_model_directory(base_path))
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)
self.assertTrue(loader.maybe_saved_model_directory(base_path))
base_path = "complete_garbage"
self.assertFalse(loader.maybe_saved_model_directory(base_path))
