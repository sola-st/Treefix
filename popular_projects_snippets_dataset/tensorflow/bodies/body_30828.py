# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
labels = np.zeros([0, 2, 4]).astype(np.float32)
logits = np.zeros([0, 2, 4]).astype(np.float32)
np_loss, _ = self._npXent(labels=labels, logits=logits)
loss = nn_ops.softmax_cross_entropy_with_logits(
    labels=labels, logits=logits)
tf_loss = self.evaluate(loss)
self.assertAllEqual(np_loss, tf_loss)
