# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
s = math_ops.sobol_sample(dim, 100, dtype=dtypes.float32)
assert s.shape.as_list() == [100, None]
exit(s)
