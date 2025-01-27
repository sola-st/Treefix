# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
counts, probs = np.broadcast_arrays(self.counts, self.probs)
broadcast_shape = counts.shape

counts = np.reshape(counts, (-1,))
probs = np.reshape(probs, (-1,))
counts_and_probs = np.stack([counts, probs], axis=-1)
moments = np.fromiter(
    (stats.binom(cp[0], cp[1]).moment(i) for cp in counts_and_probs),
    dtype=np.float64)
exit(np.reshape(moments, broadcast_shape))
