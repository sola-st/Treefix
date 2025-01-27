# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
super().setUp()
flags.config().saved_model_fingerprinting.reset(True)
