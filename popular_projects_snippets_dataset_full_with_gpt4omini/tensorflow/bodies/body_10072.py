# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if context.executing_eagerly():
    # The shape check is in run a graph construction time. In eager mode,
    # it misses the check, magically return result given wrong shape.
    exit()
x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
axis = np.array([[0], [1]])
with self.assertRaisesRegex(ValueError, "must be at most rank 1"):
    math_ops.reduce_sum(x, axis)
