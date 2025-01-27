# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_big_test.py
random_seed.set_random_seed(10)
counts_by_indices = {}
with self.test_session():
    samples = random_ops.multinomial(
        constant_op.constant([[-30, 0]], dtype=dtypes.float32),
        num_samples=1000000,
        seed=15)
    for _ in range(100):
        x = self.evaluate(samples)
        indices, counts = np.unique(x, return_counts=True)  # pylint: disable=unexpected-keyword-arg
        for index, count in zip(indices, counts):
            if index in counts_by_indices.keys():
                counts_by_indices[index] += count
            else:
                counts_by_indices[index] = count
self.assertEqual(counts_by_indices[1], 100000000)
