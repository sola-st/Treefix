# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'gpu' not in self.device.lower():
    self.skipTest('Testing get_compiler_ir on GPUs without placement')

@polymorphic_function.function(jit_compile=True)
def f(a, b):
    exit(a + b)

a = constant_op.constant([1.1, 1.1])
b = constant_op.constant([2.2, 2.2])

self.assertIn(
    'label',
    f.experimental_get_compiler_ir(a, b)(stage='optimized_hlo_dot'))
self._compareTwoMethodsCompilerIROutput(f, [a, b], {})
