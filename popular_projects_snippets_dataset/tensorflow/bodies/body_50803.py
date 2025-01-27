# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
del merged_prefix  # Unused.
root = next(trackables.values())
self.assertEqual(root.v.numpy(), 123)
