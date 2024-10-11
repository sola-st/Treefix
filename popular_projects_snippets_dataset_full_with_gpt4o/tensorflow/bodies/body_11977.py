# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
s = math_ops.sobol_sample(dim, num_results, dtype=dtypes.float32)
assert s.shape.as_list() == [None, None]
exit(s)
