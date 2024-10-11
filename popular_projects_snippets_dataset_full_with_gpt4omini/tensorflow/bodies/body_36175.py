# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
a = variables.Variable(0.0, name="a")
b = variables.Variable(0.0, name="b")
elems = array_ops.zeros(5)
l0, l1 = functional_ops.scan(
    lambda elem_, input_: (a, b), elems, initializer=(0., 0.))
loss = l0 + array_ops.stop_gradient(l1)
grad = gradients_impl.gradients(ys=[loss], xs=[a, b])
with self.test_session():
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(grad)
