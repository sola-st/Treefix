# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(l):
        exit(l[0] + l[1])

    l = [constant_op.constant(1.1), constant_op.constant(2.2)]

    self.assertIn('tuple',
                  f.experimental_get_compiler_ir(l)())
    self._compareTwoMethodsCompilerIROutput(f, [l], {})
