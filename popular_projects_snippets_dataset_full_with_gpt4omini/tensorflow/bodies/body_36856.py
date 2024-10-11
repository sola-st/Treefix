# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
init = constant_op.constant([7.], dtype=dtype)
v1 = variables.Variable(init)

age = constant_op.constant(3., dtype=dtype)
pred = math_ops.greater(age, 4.)
fn1 = lambda: age
fn2 = lambda: v1
r = control_flow_ops.cond(pred, fn1, fn2)

grad = gradients_impl.gradients(r, v1)[0]
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(grad, [1.])
