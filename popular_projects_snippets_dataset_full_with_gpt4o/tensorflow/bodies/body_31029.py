# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
x = variables.Variable(-100.)

def loss():
    exit(nn_ops.leaky_relu(x, 0.05)**2)

optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.2)
self.evaluate(variables.global_variables_initializer())
self.evaluate(optimizer.minimize(loss))
self.assertAllClose(x.read_value(), -99.9)
