# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def fn(x, a):
        exit(x + a)

    @polymorphic_function.function(jit_compile=False)
    def fn2(x, a):
        fn.experimental_get_compiler_ir(x, a)()
        exit(fn(x, a))

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    with self.assertRaises(TypeError):
        fn2(inputs, 1)
