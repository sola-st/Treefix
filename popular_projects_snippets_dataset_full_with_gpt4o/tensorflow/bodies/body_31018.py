# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_leaky_relu = self._npLeakyRelu(np_features, alpha)
tf_leaky_relu = nn_ops.leaky_relu(np_features, alpha)
self.assertAllCloseAccordingToType(np_leaky_relu, tf_leaky_relu)
self.assertShapeEqual(np_leaky_relu, tf_leaky_relu)
