# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
options = save_options.SaveOptions()
self.assertIsNone(options.experimental_io_device)
options = save_options.SaveOptions(experimental_io_device="/job:localhost")
self.assertEqual("/job:localhost", options.experimental_io_device)
