# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.array([1, 2, 3, 4]).reshape(2, 2).astype(np.float32)
y = np.array([1, 2]).reshape(2, 1).astype(np.float32)
with self.cached_session() as sess:
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y)
    s = math_ops.reduce_sum(inx * iny)
    gx, gy = sess.run(gradients_impl.gradients(s, [inx, iny]))
# gx is simply the broadcasted y
self.assertAllEqual(gx,
                    np.array([1, 1, 2, 2]).reshape(2, 2).astype(np.float32))
# gy is x's column summed up
self.assertAllEqual(gy, np.array([3, 7]).reshape(2, 1).astype(np.float32))
