# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        exit(math_ops.argmax(x))

    inputs = array_ops.ones([10], dtype=dtypes.float32)
    hlo = f.experimental_get_compiler_ir(inputs)(stage='hlo')

    # Test that reduction occurs only once.
    self.assertGreater(hlo.count('reduce'), 1)
    self._compareTwoMethodsCompilerIROutput(f, [inputs], {})
