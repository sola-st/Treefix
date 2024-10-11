# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
base_operator = linalg.LinearOperatorIdentity(num_rows=3, dtype=np.float64)
u = rng.rand(5, 3, 2)
diag = rng.rand(5, 4)  # Last dimension should be 2
with self.assertRaisesRegex(ValueError, "not compatible"):
    linalg.LinearOperatorLowRankUpdate(base_operator, u=u, diag_update=diag)
