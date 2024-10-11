# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_big_test.py
random_seed.set_random_seed(10)
counts_by_indices = {}
# here the cpu undersamples and won't pass this test either
with self.test_session():
    samples = random_ops.multinomial(
        constant_op.constant([[0, -17]], dtype=dtypes.float32),
        num_samples=1000000,
        seed=22)

    # we'll run out of memory if we try to draw 1e9 samples directly
    # really should fit in 12GB of memory...
    for _ in range(100):
        x = self.evaluate(samples)
        indices, counts = np.unique(x, return_counts=True)  # pylint: disable=unexpected-keyword-arg
        for index, count in zip(indices, counts):
            if index in counts_by_indices.keys():
                counts_by_indices[index] += count
            else:
                counts_by_indices[index] = count
self.assertGreater(counts_by_indices[1], 0)
