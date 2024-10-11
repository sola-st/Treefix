# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
with self.assertRaisesRegex(ValueError, "No or invalid fingerprint"):
    read_fingerprint("foo")
