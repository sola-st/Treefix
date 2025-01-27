# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
# Create an op without specifying the dtype. Dtype should be float32 in
# this case.
s = math_ops.sobol_sample(10, 100)
self.assertEqual(dtypes.float32, s.dtype)
