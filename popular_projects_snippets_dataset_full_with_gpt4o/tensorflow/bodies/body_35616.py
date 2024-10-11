# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
with test_util.use_gpu():
    shape = [5, 4, 1]
    size = np.prod(shape)
    single = [1, 1, 1]
    value = np.arange(size).reshape(shape)
    iterations = 5
    num_samples = 5

    # Test that the same result is returned given the same seed is provided
    # for each round.
    test_seed = (1, 2)
    observations = [[] for _ in range(iterations)]
    for observation in observations:
        crop = random_ops.stateless_random_crop(value, single, seed=test_seed)
        counts = np.zeros(size, dtype=np.int32)
        for _ in range(num_samples):
            y = self.evaluate(crop)
            self.assertAllEqual(y.shape, single)
            counts[y] += 1

        observation.append(counts)

    for i in range(1, iterations):
        self.assertAllEqual(observations[0], observations[i])

    # Test that the same sequence of results are returned given the same
    # sequence of seeds provided.
    test_seeds = [
        tuple(map(lambda x, i=i: x + 1 * i, t))
        for (i, t) in enumerate((1, 2) for _ in range(iterations))
    ]
    observations = [[] for _ in range(iterations)]
    for observation in observations:
        counts = np.zeros(size, dtype=np.int32)
        for seed in test_seeds:
            crop = random_ops.stateless_random_crop(
                value, single, seed=seed)
            y = self.evaluate(crop)
            self.assertAllEqual(y.shape, single)
            counts[y] += 1

        observation.append(counts)

    for i in range(1, iterations):
        self.assertAllEqual(observations[0], observations[i])
