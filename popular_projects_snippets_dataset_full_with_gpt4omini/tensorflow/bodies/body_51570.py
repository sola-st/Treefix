# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
options = load_options.LoadOptions()
self.assertIsNone(options.experimental_io_device)
options = load_options.LoadOptions(experimental_io_device="/job:localhost")
self.assertEqual("/job:localhost", options.experimental_io_device)
