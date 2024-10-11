# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
super(MeanPairwiseSquaredErrorTest, self).setUp()
self._predictions = np.array([[4, 8, 12], [8, 1, 3]])
self._labels = np.array([[1, 9, 2], [-5, -5, 7]])

batch_size, dims = self._labels.shape  # pylint: disable=unpacking-non-sequence

# Compute the expected loss 'manually'.
total = np.zeros((batch_size,))
for b in range(batch_size):
    for i in range(dims - 1):
        for j in range(i + 1, dims):
            x = self._predictions[b, i].item() - self._predictions[b, j].item()
            y = self._labels[b, i].item() - self._labels[b, j].item()
            diff = (x - y)
            total[b] += (diff * diff)

self._expected_losses = np.divide(total, 3.0)
