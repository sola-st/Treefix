# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
img = constant_op.constant(
    np.arange(25).reshape((1, 5, 5, 1)), dtype=dtypes.float32)
with self.test_session():
    result1 = image_ops.extract_glimpse_v2(
        img, [3, 3], [[0, 0]], centered=False, normalized=False)
    result2 = image_ops.extract_glimpse_v2(
        img, [3, 3], [[1, 0]], centered=False, normalized=False)
    self.assertAllEqual(
        np.asarray([[0, 1, 2], [5, 6, 7], [10, 11, 12]]),
        self.evaluate(result1)[0, :, :, 0])
    self.assertAllEqual(
        np.asarray([[5, 6, 7], [10, 11, 12], [15, 16, 17]]),
        self.evaluate(result2)[0, :, :, 0])
