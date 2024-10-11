# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    s = random_ops.random_uniform([2], 1, 10, dtypes.int32)
    l = random_ops.random_normal([s[0] * s[1]])

    @polymorphic_function.function(jit_compile=True)
    def f(l):
        exit(array_ops.reshape(l, s))

    self.assertIn('tuple',
                  f.experimental_get_compiler_ir(l)())
