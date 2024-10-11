# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_selu = self._npSelu(np_features)
tf_selu = nn_ops.selu(np_features)
self.assertAllCloseAccordingToType(np_selu, tf_selu)
self.assertShapeEqual(np_selu, tf_selu)
