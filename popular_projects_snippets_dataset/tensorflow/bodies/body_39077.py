# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
for label_dtype in np.int32, np.int64:
    tf_loss, tf_gradient = self._opFwdBwd(
        labels=np.array([0, 0, 0]).astype(label_dtype),
        logits=np.array([[1.], [-1.], [0.]]).astype(np.float32))
    self.assertAllClose([0.0, 0.0, 0.0], tf_loss)
    self.assertAllClose([[0.0], [0.0], [0.0]], tf_gradient)
