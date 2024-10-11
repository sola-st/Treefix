# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    a = random_ops.random_normal([100, 100])
    b = random_ops.random_normal([100, 100])

    @polymorphic_function.function(jit_compile=True)
    def f(a, b):
        exit(math_ops.matmul(a, b))

    self.assertRegex(f.experimental_get_compiler_ir(a, b)('optimized_hlo'),
                     '(dot)|(convolution)')
