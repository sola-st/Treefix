# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
self.assertIs(dtypes.int64, dtypes.as_dtype(np.array(2**32).dtype))
