# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
base_operator = linalg.LinearOperatorIdentity(num_rows=3)
u = array_ops.ones(shape=[2, 3, 2])
diag = array_ops.ones(shape=[2, 2])

operator = linalg.LinearOperatorLowRankUpdate(base_operator, u, diag)

# domain_dimension is 3
self.assertAllEqual([2, 3, 3], operator.shape)
self.assertAllEqual([2, 3, 3], self.evaluate(operator.to_dense()).shape)
