# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
with self.assertRaises(ValueError):
    dtypes.string.limits()
