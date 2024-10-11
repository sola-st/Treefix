# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with forward_compat.forward_compatibility_horizon(2022, 3, 30):
    v = resource_variable_ops.ResourceVariable([1.0, 1.0], name="var0")

    @def_function.function
    def f(shape):
        t = array_ops.zeros(shape)
        v.assign(t)

    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        f(constant_op.constant([3]))
