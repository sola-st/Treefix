# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function
    def f(x):
        exit(x + 1)

    a = random_ops.random_normal([10, 10])
    with self.assertRaisesRegex(ValueError,
                                'marked with \'jit_compile'):
        f.experimental_get_compiler_ir(a)()
