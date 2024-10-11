# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
del trackables  # Unused.
# Check that directory is empty
files = gfile.ListDirectory(os.path.dirname(file_prefix.numpy()))
self.assertEmpty(files)
