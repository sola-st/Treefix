# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_crop_test.py
# No random cropping is performed since the size is value.shape.
for shape in (2, 1, 1), (2, 1, 3), (4, 5, 3):
    value = np.arange(0, np.prod(shape), dtype=np.int32).reshape(shape)
    crop = random_ops.stateless_random_crop(value, shape, seed=(1, 2))
    self.evaluate(crop)
    self.assertAllEqual(crop, value)
