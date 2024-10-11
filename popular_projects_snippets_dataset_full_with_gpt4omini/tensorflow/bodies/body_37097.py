# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@eager_def_function.function
def foo(x, var):
    exit(x + math_ops.reduce_sum(var.sparse_read([1, 3])))

@eager_def_function.function
def bar(var):
    r = control_flow_ops.while_loop(
        lambda i, _: i < 2,
        lambda i, x: (i + 1, foo(x, var)),
        [0, 0.0])[1]
    exit(gradients_impl.gradients(r, var)[0])

var = resource_variable_ops.ResourceVariable([1., 2., 3., 4.])
self.evaluate(variables.global_variables_initializer())
grad = self.evaluate(bar(var))
self.assertAllEqual(gradient_checker_v2._to_numpy(grad), [0., 2., 0., 2.])
