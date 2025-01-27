# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
# Run 1x1 crop num_samples times in an image and ensure that one finds each
# pixel 1/size of the time.
num_samples = 1000
shape = [5, 4, 1]
size = np.prod(shape)
single = [1, 1, 1]
value = np.arange(size).reshape(shape)

with self.cached_session():
    crop = random_ops.random_crop(value, single, seed=7)
    counts = np.zeros(size, dtype=np.int32)
    for _ in range(num_samples):
        y = self.evaluate(crop)
        self.assertAllEqual(y.shape, single)
        counts[y] += 1

    # Calculate the mean and 4 * standard deviation.
mean = np.repeat(num_samples / size, size)
four_stddev = 4.0 * np.sqrt(mean)

# Ensure that each entry is observed in 1/size of the samples
# within 4 standard deviations.
self.assertAllClose(counts, mean, atol=four_stddev)
