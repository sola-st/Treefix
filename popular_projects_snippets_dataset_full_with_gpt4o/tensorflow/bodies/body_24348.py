# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
# In the non-pip world, code resides in "tensorflow/"
# In the pip world, after virtual pip, code resides in "tensorflow_core/"
# So, we have to check both of them
self.assertIn(
    os.path.basename(source_utils._TENSORFLOW_BASEDIR),
    ["tensorflow", "tensorflow_core"])
