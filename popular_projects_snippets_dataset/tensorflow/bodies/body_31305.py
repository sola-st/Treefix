# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test.py
np_f = np.array([[1., 2., 3., 4.],
                 [1., 2., 3., 4.]]).astype(np.float32)
np_l = np.array([[0., 0., 0., 1.],
                 [0., .5, .5, 0.]]).astype(np.float32)
np_loss, np_gradient = self._npXent(labels=np_l, logits=np_f)
tf_f = constant_op.constant(
    np.array([[1., 2., 3., 4.]]).astype(np.float32))
tf_l = constant_op.constant(
    np.array([[0., 0., 0., 1.], [0., .5, .5, 0.]]).astype(np.float32))
tf_loss, tf_gradient = gen_nn_ops.softmax_cross_entropy_with_logits(
    tf_f, tf_l)
self.assertAllCloseAccordingToType(np_loss, tf_loss)
self.assertAllCloseAccordingToType(np_gradient, tf_gradient)

tf_f = constant_op.constant(np.array([[1.]]).astype(np.float32))
tf_l = constant_op.constant(np.array([[1.], [1.]]).astype(np.float32))
tf_loss, tf_gradient = gen_nn_ops.softmax_cross_entropy_with_logits(
    tf_f, tf_l)
self.assertAllClose([0, 0], tf_loss)
self.assertAllCloseAccordingToType([[0], [0]], tf_gradient)
