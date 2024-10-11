# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
self.assertTrue(flags.config().saved_model_fingerprinting.value())
flags.config().saved_model_fingerprinting.reset(False)
self.assertFalse(flags.config().saved_model_fingerprinting.value())
