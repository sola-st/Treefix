# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
x = random_ops.random_uniform([2, 3, 5])
y = x * x
batch_jacobian_pfor = gradients.batch_jacobian(y, x, use_pfor=True)
batch_jacobian_while = gradients.batch_jacobian(y, x, use_pfor=False)
two_x = 2 * x
answer = array_ops.stack(
    [array_ops.diag(two_x[0]),
     array_ops.diag(two_x[1])])
self.run_and_assert_equal(answer, batch_jacobian_pfor)
self.run_and_assert_equal(answer, batch_jacobian_while)
