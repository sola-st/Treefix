# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def fn(x, y):
        exit(x + y)

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    self.assertIn('polymorphic_function_xla_jit_test',
                  fn.experimental_get_compiler_ir(inputs, inputs)())
    self._compareTwoMethodsCompilerIROutput(fn, [inputs, inputs], {})
