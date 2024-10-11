# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(a, b):
        exit(a + b)

    a = constant_op.constant([1.1, 1.1])
    b = constant_op.constant([2.2, 2.2])

    self.assertIn(
        'label',
        f.experimental_get_compiler_ir(a, b)(stage='optimized_hlo_dot'))
    self._compareTwoMethodsCompilerIROutput(f, [a, b], {})
