# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
self.mean = mean
self.stddev = stddev
self.seed = seed
self.dtype = _assert_float_dtype(dtypes.as_dtype(dtype))
