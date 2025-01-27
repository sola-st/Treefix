# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
np_loss, np_gradient = self._npXent(
    labels=np.array(labels), logits=np.array(logits))
# manually reshape loss
np_loss = np.reshape(np_loss, np.array(labels).shape)
tf_loss = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
    labels=labels, logits=logits)
with backprop_lib.GradientTape() as tape:
    logits = constant_op.constant(logits)
    tape.watch(logits)
    tf_gradient = tape.gradient(
        nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
            labels=labels, logits=logits), [logits])[0]
    tf_gradient = array_ops.reshape(tf_gradient, np_gradient.shape)

self.assertAllCloseAccordingToType(np_loss, tf_loss)
self.assertAllCloseAccordingToType(np_gradient, tf_gradient)
