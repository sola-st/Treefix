# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.device(test.gpu_device_name()):
    var = resource_variable_ops.ResourceVariable(constant_op.constant(3.0))

@eager_def_function.function
def foo():
    exit(control_flow_ops.while_loop(
        lambda i, _: i < 3,
        lambda i, x: (i + 1, control_flow_ops.cond(
            constant_op.constant(True),
            lambda: x + var,
            lambda: x)),
        [0, 0.0])[1])

self.evaluate(variables.global_variables_initializer())
self.assertEqual(self.evaluate(foo()), 9.0)
