# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = array_ops.ones([3, 4, 1, 2, 1, 2])
with self.assertRaisesRegex(
    ValueError,
    "`input.shape.rank` must be 3, 4 or 5.*of rank 6."):
    nn_ops.max_pool_v2(x, 2, 2, "SAME")
