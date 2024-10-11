# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
with self.cached_session():
    n = array_ops.placeholder_with_default(-2, shape=None)
    with self.assertRaisesError("must be non-negative"):
        operator = linalg_lib.LinearOperatorZeros(
            num_rows=n, assert_proper_shapes=True)
        self.evaluate(operator.to_dense())
