# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils_test.py
saved_model_dir = os.path.join(test.get_temp_dir(), "invalid_saved_model")
with self.assertRaisesRegex(
    IOError, "SavedModel file does not exist at: %s" % saved_model_dir):
    saved_model_utils.read_saved_model(saved_model_dir)
