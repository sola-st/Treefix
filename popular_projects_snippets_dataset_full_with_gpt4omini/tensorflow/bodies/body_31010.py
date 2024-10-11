# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_relu6 = self._npRelu6(np_features)
tf_relu6 = nn_ops.relu6(np_features)
self.assertAllClose(np_relu6, tf_relu6)
self.assertShapeEqual(np_relu6, tf_relu6)
