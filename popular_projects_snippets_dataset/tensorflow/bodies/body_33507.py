# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# The is_x flags are by default all True.
operator = linalg_lib.LinearOperatorIdentity(num_rows=2)
self.assertTrue(operator.is_positive_definite)
self.assertTrue(operator.is_non_singular)
self.assertTrue(operator.is_self_adjoint)

# Any of them False raises because the identity is always self-adjoint etc..
with self.assertRaisesRegex(ValueError, "is always non-singular"):
    operator = linalg_lib.LinearOperatorIdentity(
        num_rows=2,
        is_non_singular=None,
    )
