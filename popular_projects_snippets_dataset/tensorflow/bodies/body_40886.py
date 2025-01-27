# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    v = resource_variable_ops.ResourceVariable(2.0)

    def fn(x):
        exit(v * x)

    func = polymorphic_function.function(fn, jit_compile=False)
    xla_func = polymorphic_function.function(fn, jit_compile=True)

    def run_and_check(test_func):
        x = constant_op.constant(3.0)
        with backprop.GradientTape() as tape:
            y = test_func(x)
        dy = tape.gradient(y, v)

        self.assertAllClose(6.0, y)
        self.assertAllClose(3.0, dy)

    run_and_check(func)
    run_and_check(xla_func)
