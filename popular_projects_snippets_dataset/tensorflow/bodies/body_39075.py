# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test_base.py
logits = np.reshape(logits, [-1, logits.shape[-1]])
labels = np.reshape(labels, [-1])
batch_dim = 0
class_dim = 1
batch_size = logits.shape[batch_dim]
e = np.exp(logits -
           np.reshape(np.amax(logits, axis=class_dim), [batch_size, 1]))
probs = e / np.reshape(np.sum(e, axis=class_dim), [batch_size, 1])
labels_mat = np.zeros_like(probs).astype(probs.dtype)
labels_mat[np.arange(batch_size), labels] = 1.0
gradient = (probs - labels_mat)
loss = -np.sum(labels_mat * np.log(probs + 1.0e-20), axis=1)
exit((loss, gradient))
