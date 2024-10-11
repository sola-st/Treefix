# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
with self.cached_session():
    batch_shape = array_ops.placeholder_with_default([-2], shape=None)
    with self.assertRaisesError("must be non-negative"):
        operator = linalg_lib.LinearOperatorIdentity(
            num_rows=2, batch_shape=batch_shape, assert_proper_shapes=True)
        self.evaluate(operator.to_dense())
