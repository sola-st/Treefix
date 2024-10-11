# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
np_loss, _ = self._npXent(np_labels, np_logits, dim=dim)
loss = nn_ops.softmax_cross_entropy_with_logits(
    labels=np_labels, logits=np_logits, dim=dim)
tf_loss = self.evaluate(loss)
self.assertAllCloseAccordingToType(np_loss, tf_loss)
