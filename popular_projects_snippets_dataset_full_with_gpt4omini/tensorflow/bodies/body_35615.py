# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
with test_util.use_gpu():
    shape = (3, 5, 7)
    target = (2, 3, 4)
    value = np.random.randint(1000000, size=shape)
    iterations = 10
    value_set = set(
        tuple(value[i:i + 2, j:j + 3, k:k + 4].ravel())  # pylint: disable=g-complex-comprehension
        for i in range(2) for j in range(3) for k in range(4))
    test_seeds = [
        tuple(map(lambda x, i=i: x + 1 * i, t))
        for (i, t) in enumerate((1, 2) for _ in range(iterations))
    ]

    # Check that the result is valid by making sure that it is one of all
    # possible values for randomly cropping `value` with `target` shape.
    for seed in test_seeds:
        crop = random_ops.stateless_random_crop(value, size=target, seed=seed)
        y = self.evaluate(crop)
        self.assertAllEqual(y.shape, target)
        self.assertIn(tuple(y.ravel()), value_set)
