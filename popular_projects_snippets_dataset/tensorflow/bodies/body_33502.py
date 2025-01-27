# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
num_rows = array_ops.placeholder_with_default(2, shape=None)
x = array_ops.placeholder_with_default(
    rng.rand(3, 3).astype(np.float32), shape=None)

with self.cached_session():
    with self.assertRaisesError("Dimensions.*not.compatible"):
        operator = linalg_lib.LinearOperatorIdentity(
            num_rows, assert_proper_shapes=True)
        self.evaluate(operator.matmul(x))
