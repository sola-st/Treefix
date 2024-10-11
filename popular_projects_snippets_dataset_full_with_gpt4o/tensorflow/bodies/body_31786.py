# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softplus_op_test.py
np_softplus = self._npSoftplus(np_features)
with self.cached_session(use_gpu=use_gpu):
    softplus = nn_ops.softplus(np_features)
    tf_softplus = self.evaluate(softplus)
self.assertAllCloseAccordingToType(
    np_softplus, tf_softplus, bfloat16_rtol=5e-2, bfloat16_atol=5e-2
)
self.assertTrue(np.all(tf_softplus > 0))
self.assertShapeEqual(np_softplus, softplus)
