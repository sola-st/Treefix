# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
# A previous version of the code checked the op name rather than the op type
# to distinguish between log and non-log.  Use an arbitrary name to catch
# this bug in future.
name = "arbitrary"
np_softmax = self._npSoftmax(np_features, dim=dim, log=log)
with self.cached_session(use_gpu=use_gpu):
    if dtype is not None:
        np_features = math_ops.cast(np_features, dtype=dtype)

    if log:
        tf_softmax = nn_ops.log_softmax(np_features, axis=dim, name=name)
    else:
        tf_softmax = nn_ops.softmax(np_features, axis=dim, name=name)
    out = self.evaluate(tf_softmax)
self.assertAllCloseAccordingToType(np_softmax, out)
self.assertShapeEqual(np_softmax, tf_softmax)
if not log and dtype is None:
    # Bonus check: the softmaxes should add to one in dimension dim.
    sum_along_dim = np.sum(out, axis=dim)
    self.assertAllCloseAccordingToType(
        np.ones(sum_along_dim.shape), sum_along_dim)
