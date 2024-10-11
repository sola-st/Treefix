# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
np_loss, np_gradient = self._npXent(labels=np_labels, logits=np_logits)
if expected_gradient is not None:
    np_gradient = expected_gradient
with self.cached_session() as sess:
    if with_placeholders:
        logits_placeholder = array_ops.placeholder(np_logits.dtype)
        labels_placeholder = array_ops.placeholder(np_labels.dtype)
        loss, gradient = self._opFwdBwd(labels_placeholder, logits_placeholder)
        tf_loss, tf_gradient = sess.run([loss, gradient],
                                        feed_dict={
                                            labels_placeholder: np_labels,
                                            logits_placeholder: np_logits
                                        })
    else:
        loss, gradient = self._opFwdBwd(np_labels, np_logits)
        tf_loss, tf_gradient = self.evaluate([loss, gradient])
self.assertAllCloseAccordingToType(np_loss, tf_loss, half_rtol=1e-2)
self.assertAllCloseAccordingToType(np_gradient, tf_gradient)
