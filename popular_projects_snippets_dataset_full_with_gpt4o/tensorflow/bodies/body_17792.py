# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32, shape=[None, None])
    y = math_ops.matmul(x, x, transpose_a=True)
    jacobian_pfor = gradients.jacobian(y, x, use_pfor=True)
    jacobian_while = gradients.jacobian(y, x, use_pfor=False)
    answer = ops.convert_to_tensor([[
        gradient_ops.gradients(y[0][0], x)[0],
        gradient_ops.gradients(y[0][1], x)[0]
    ], [
        gradient_ops.gradients(y[1][0], x)[0],
        gradient_ops.gradients(y[1][1], x)[0]
    ]])
    ans, pfor_value, while_value = sess.run(
        [answer, jacobian_pfor, jacobian_while],
        feed_dict={x: [[1, 2], [3, 4]]})
    self.assertAllClose(ans, pfor_value)
    self.assertAllClose(ans, while_value)
