# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
# Note: The old versions of extract_glimpse was incorrect in implementation.
# This test is for compatibility so that graph save in old versions behave
# the same. Notice the API uses gen_image_ops.extract_glimpse() on purpose.
#
# Image:
# [  0.   1.   2.   3.   4.]
# [  5.   6.   7.   8.   9.]
# [ 10.  11.  12.  13.  14.]
# [ 15.  16.  17.  18.  19.]
# [ 20.  21.  22.  23.  24.]
img = constant_op.constant(
    np.arange(25).reshape((1, 5, 5, 1)), dtype=dtypes.float32)
with self.test_session():
    # Result 1:
    # [ 0.  0.  0.]
    # [ 0.  0.  0.]
    # [ 0.  0.  0.]
    result1 = gen_image_ops.extract_glimpse(
        img, [3, 3], [[-2, 2]],
        centered=False,
        normalized=False,
        noise='zero',
        uniform_noise=False)
    self.assertAllEqual(
        np.asarray([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        self.evaluate(result1)[0, :, :, 0])

    # Result 2:
    # [  0.   0.   0.   0.   0.   0.   0.]
    # [  0.   0.   1.   2.   3.   4.   0.]
    # [  0.   5.   6.   7.   8.   9.   0.]
    # [  0.  10.  11.  12.  13.  14.   0.]
    # [  0.  15.  16.  17.  18.  19.   0.]
    # [  0.  20.  21.  22.  23.  24.   0.]
    # [  0.   0.   0.   0.   0.   0.   0.]
    result2 = gen_image_ops.extract_glimpse(
        img, [7, 7], [[0, 0]],
        normalized=False,
        noise='zero',
        uniform_noise=False)
    self.assertAllEqual(
        np.asarray([[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 4, 0],
                    [0, 5, 6, 7, 8, 9, 0], [0, 10, 11, 12, 13, 14, 0],
                    [0, 15, 16, 17, 18, 19, 0], [0, 20, 21, 22, 23, 24, 0],
                    [0, 0, 0, 0, 0, 0, 0]]),
        self.evaluate(result2)[0, :, :, 0])
