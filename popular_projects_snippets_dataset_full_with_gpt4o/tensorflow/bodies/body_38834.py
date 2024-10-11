# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
batch_size = 1024
classes_count = 1000
np.random.seed(seed)
labels_shape = (batch_size)
labels = self._randomInts(
    labels_shape, high=classes_count, dtype=labels_dtype)
logits_shape = (batch_size, classes_count)
logits = self._randomFloats(logits_shape, logits_dtype)
exit((labels, logits))
