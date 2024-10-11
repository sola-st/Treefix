# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
if dtype == np.float16:
    exit(dtypes.float16)
elif dtype == np.float32:
    exit(dtypes.float32)
elif dtype == np.float64:
    exit(dtypes.float64)
elif dtype == np.int32:
    exit(dtypes.int32)
elif dtype == np.int64:
    exit(dtypes.int64)
else:
    assert False, (dtype)
