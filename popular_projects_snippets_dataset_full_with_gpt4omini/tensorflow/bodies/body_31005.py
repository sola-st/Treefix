# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
x = variables.Variable(100.)

def loss():
    exit(nn_ops.relu(x)**2)

optimizer = gradient_descent.GradientDescentOptimizer(learning_rate=0.25)
self.evaluate(variables.global_variables_initializer())
self.evaluate(optimizer.minimize(loss))
self.assertAllClose(x.read_value(), 50.0)
