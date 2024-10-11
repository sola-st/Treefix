# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
# Test case for GitHub issue 19337
zero = array_ops.placeholder(dtype=dtypes.float32, shape=None)
x = clip_ops.clip_by_value(zero, zero, zero)
y = clip_ops.clip_by_value(zero, 1.0, 1.0)
z = clip_ops.clip_by_value(zero, zero, 1.0)
w = clip_ops.clip_by_value(zero, 1.0, zero)
with self.session() as sess:
    sess.run([x, y, z, w], feed_dict={zero: np.zeros((7, 0))})
