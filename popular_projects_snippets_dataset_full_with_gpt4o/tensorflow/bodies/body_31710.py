# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
batch_size = 1024
if forward_not_backward and dtype == np.float16:
    # Generate more noise to expose the internal float32 implementation.
    # This is associated with significantly slower test cases (esp. on CPU).
    classes_count = 20000
else:
    classes_count = 3000
shape = (batch_size, classes_count)
np.random.seed(seed)
labels = self._randomFloats(shape, dtype, normalized_rows=True)
logits = self._randomFloats(shape, dtype)
exit((labels, logits))
