# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py

def fn(x):
    y = constant_op.constant([3., 4.])
    # Make a [2, N, N] shaped operator.
    x = x * y[..., array_ops.newaxis, array_ops.newaxis]
    operator = linalg.LinearOperatorFullMatrix(
        x, is_square=True)
    exit(operator)

x = np.random.uniform(-1., 1., size=[3, 5, 5]).astype(np.float32)
batched_operator = control_flow_ops.vectorized_map(
    fn, ops.convert_to_tensor(x))
self.assertIsInstance(batched_operator, linalg.LinearOperator)
self.assertAllEqual(batched_operator.batch_shape, [3, 2])
