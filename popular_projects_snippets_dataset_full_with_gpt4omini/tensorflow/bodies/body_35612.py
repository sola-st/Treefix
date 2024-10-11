# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
with self.cached_session():
    shape = (3, 5, 7)
    target = (2, 3, 4)
    value = np.random.randint(1000000, size=shape)
    value_set = set(
        tuple(value[i:i + 2, j:j + 3, k:k + 4].ravel())
        for i in range(2) for j in range(3) for k in range(4))
    crop = random_ops.random_crop(value, size=target)
    for _ in range(20):
        y = self.evaluate(crop)
        self.assertAllEqual(y.shape, target)
        self.assertTrue(tuple(y.ravel()) in value_set)
