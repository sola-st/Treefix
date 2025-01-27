# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest("No GPU available")
inputs = constant_op.constant(
    np.array([[-50, 7, 23], [0, 1, -5], [6, -2, 11]]), dtypes.qint8)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Tensor size must be a multiple of 4 for Relu<qint8>. Got 9"):
    self.evaluate(nn_ops.relu(inputs))

inputs = constant_op.constant(
    np.array([1, -2, 3, -4, 5, -6, 7, -8, 9, -8, 7, -6, 5, -4, 3, -2, 1]),
    dtypes.qint8)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Tensor size must be a multiple of 4 for Relu<qint8>. Got 17"):
    self.evaluate(nn_ops.relu(inputs))
