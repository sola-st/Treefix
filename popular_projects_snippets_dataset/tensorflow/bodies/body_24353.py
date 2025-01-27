# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
self.assertFalse(
    source_utils.guess_is_tensorflow_py_library(
        os.path.join(os.path.dirname(self.curr_file_path), "foo.cc")))
