# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
with test_util.device(use_gpu=True):
    for axis in (0, -2):
        self.assertAllEqual(
            self.evaluate(math_ops.reduce_sum(x, axis=axis)), [5, 7, 9])
    for axis in (1, -1):
        self.assertAllEqual(
            self.evaluate(math_ops.reduce_sum(x, axis=axis)), [6, 15])
    for axis in (None, (0, 1), (1, 0), (-1, 0), (0, -1), (-2, 1), (1, -2),
                 (-1, -2), (-2, -1)):
        self.assertEqual(self.evaluate(math_ops.reduce_sum(x, axis=axis)), 21)
