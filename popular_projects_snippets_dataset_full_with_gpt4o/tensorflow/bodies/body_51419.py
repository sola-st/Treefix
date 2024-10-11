# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if dtype:
    exit(array_ops.zeros(shape=x.shape, dtype=dtype))
else:
    exit(array_ops.zeros(shape=x.shape, dtype=dtypes.float32))
