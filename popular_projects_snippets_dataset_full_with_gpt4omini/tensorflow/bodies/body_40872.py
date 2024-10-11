# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x, y):
        exit(x + y)

    @polymorphic_function.function(jit_compile=True)
    def g(x, y):
        exit(f(x, y))

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    self.assertIn('polymorphic_function_xla_jit_test',
                  g.experimental_get_compiler_ir(inputs, inputs)())
    self._compareTwoMethodsCompilerIROutput(g, [inputs, inputs], {})
