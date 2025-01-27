# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
np_loss, np_gradient = self._npXent(labels=np_labels, logits=np_logits)
tf_loss, tf_gradient = self._opFwdBwd(labels=np_labels, logits=np_logits)
self.assertAllCloseAccordingToType(np_loss, tf_loss)
self.assertAllCloseAccordingToType(np_gradient, tf_gradient)
