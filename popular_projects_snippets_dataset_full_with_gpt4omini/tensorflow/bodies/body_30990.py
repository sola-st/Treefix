# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_relu = self._npRelu(np_features)
tf_relu = nn_ops.relu(np_features)
self.assertAllClose(np_relu, tf_relu)
self.assertShapeEqual(np_relu, tf_relu)
