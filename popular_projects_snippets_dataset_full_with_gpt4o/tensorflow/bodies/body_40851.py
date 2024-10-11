# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def fn(x, a):
        exit(x + a)

    func = polymorphic_function.function(fn, jit_compile=False)
    xla_func = polymorphic_function.function(fn, jit_compile=True)

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    self.assertAllClose([2, 3, 3, 4, 4], func(inputs, 1))
    self.assertAllClose([2, 3, 3, 4, 4], xla_func(inputs, 1))
