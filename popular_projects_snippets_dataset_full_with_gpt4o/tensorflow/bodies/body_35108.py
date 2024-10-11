# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
np_features = np.asarray(np_features)
np_softplus = self._npSoftplus(np_features)
with self.session(use_gpu=use_gpu) as sess:
    softplus = nn_ops.softplus(np_features)
    softplus_inverse = du.softplus_inverse(softplus)
    [tf_softplus, tf_softplus_inverse] = sess.run([
        softplus, softplus_inverse])
self.assertAllCloseAccordingToType(np_softplus, tf_softplus)
rtol = {"float16": 0.07, "float32": 0.003, "float64": 0.002}.get(
    str(np_features.dtype), 1e-6)
# This will test that we correctly computed the inverse by verifying we
# recovered the original input.
self.assertAllCloseAccordingToType(
    np_features, tf_softplus_inverse,
    atol=0., rtol=rtol)
self.assertAllEqual(
    np.ones_like(tf_softplus).astype(np.bool_), tf_softplus > 0)

self.assertShapeEqual(np_softplus, softplus)
self.assertShapeEqual(np_softplus, softplus_inverse)

self.assertAllEqual(
    np.ones_like(tf_softplus).astype(np.bool_), np.isfinite(tf_softplus))
self.assertAllEqual(
    np.ones_like(tf_softplus_inverse).astype(np.bool_),
    np.isfinite(tf_softplus_inverse))
