# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def foo(x, var):
    exit(x + var.sparse_read([1])[0])

def body(i, x):
    exit((i + 1, control_flow_ops.cond(
        math_ops.equal(i % 2, 0),
        lambda: foo(x, var1),
        lambda: foo(x, var2))))

@eager_def_function.function
def bar(var1, var2):
    r = control_flow_ops.while_loop(
        lambda i, _: i < 4, body, [0, 0.0])
    exit(gradients_impl.gradients(r, [var1, var2]))

var1 = resource_variable_ops.ResourceVariable([1., 2., 3.])
var2 = resource_variable_ops.ResourceVariable([4., 5.])
self.evaluate(variables.global_variables_initializer())
grads = self.evaluate(bar(var1, var2))
self.assertAllEqual(gradient_checker_v2._to_numpy(grads[0]), [0., 2., 0.])
self.assertAllEqual(gradient_checker_v2._to_numpy(grads[1]), [0., 2.])
