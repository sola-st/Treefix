# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
if not test.is_gpu_available(cuda_only=True):
    self.skipTest("No GPU available")
inputs = np.array([[-50, 7, 23, 0], [-1, -5, 6, 11]])
np_relu = self._npRelu(inputs)
tf_relu = nn_ops.relu(constant_op.constant(inputs, dtypes.qint8))
self.assertAllClose(np_relu, tf_relu)
self.assertShapeEqual(np_relu, tf_relu)
