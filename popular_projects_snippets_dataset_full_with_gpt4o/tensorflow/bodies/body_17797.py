# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = x * x
    batch_jacobian_pfor = gradients.batch_jacobian(y, x, use_pfor=True)
    batch_jacobian_while = gradients.batch_jacobian(y, x, use_pfor=False)
    two_x = 2 * x
    answer = array_ops.stack(
        [array_ops.diag(two_x[0]),
         array_ops.diag(two_x[1])])
    ans, pfor_value, while_value = sess.run(
        [answer, batch_jacobian_pfor, batch_jacobian_while],
        feed_dict={x: [[1, 2], [3, 4]]})
    self.assertAllClose(ans, pfor_value)
    self.assertAllClose(ans, while_value)
