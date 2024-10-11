# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
m3 = math_ops.matmul(m1, m2)
exit(api.relayout(m3, self.first_dimension_sharded_layout))
