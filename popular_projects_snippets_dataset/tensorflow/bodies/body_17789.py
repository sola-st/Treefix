# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
x = random_ops.random_uniform([2, 2])
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
self.run_and_assert_equal(answer, jacobian_pfor)
self.run_and_assert_equal(answer, jacobian_while)
