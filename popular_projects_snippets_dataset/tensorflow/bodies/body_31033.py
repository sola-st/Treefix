# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_elu = self._npElu(np_features)
tf_elu = nn_ops.elu(np_features)
self.assertAllCloseAccordingToType(np_elu, tf_elu)
self.assertShapeEqual(np_elu, tf_elu)
