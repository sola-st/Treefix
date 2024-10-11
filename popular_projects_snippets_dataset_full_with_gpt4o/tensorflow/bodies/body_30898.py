# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
if use_gpu:
    type = np.float32  # pylint: disable=redefined-builtin
else:
    type = np.float64  # pylint: disable=redefined-builtin
max = np.finfo(type).max  # pylint: disable=redefined-builtin
features = np.array([[1., 1., 1., 1.], [max, 1., 2., 3.]]).astype(type)
with self.cached_session(use_gpu=use_gpu):
    tf_log_softmax = nn_ops.log_softmax(features)
    out = self.evaluate(tf_log_softmax)
self.assertAllClose(
    np.array([[-1.386294, -1.386294, -1.386294, -1.386294],
              [0, -max, -max, -max]]),
    out,
    rtol=1.e-5,
    atol=1.e-5)
