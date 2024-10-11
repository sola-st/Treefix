# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
# Random shapes of rank 4, random indices
for _ in range(5):
    shape = np.random.randint(1, 20, size=4)
    indices = np.random.randint(shape[0], size=2 * shape[0])
    self._TestCase(_AsLong(list(shape)), list(indices), state_ops.scatter_sub)
