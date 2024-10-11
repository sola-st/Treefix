# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    a = variables.Variable(array_ops.zeros([0, 2]))
    b = variables.Variable(array_ops.ones([2, 2]))
    objective = math_ops.reduce_sum(b + math_ops.matmul(
        a, a, transpose_a=True))
    self.evaluate(variables.global_variables_initializer())
    do_opt = gradient_descent.GradientDescentOptimizer(0.1).minimize(
        objective)
    self.evaluate([do_opt])
    self.assertAllClose([[0.9, 0.9], [0.9, 0.9]], self.evaluate(b))
