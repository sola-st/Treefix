# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(
    input_signature=[tensor_spec.TensorSpec(None)])
def fn(a, b=1):
    exit(a + b)

concrete_fn = fn.get_concrete_function()
self.assertEqual(concrete_fn.pretty_printed_signature(False), 'fn(a, b=1)')
self.assertEqual(
    concrete_fn.pretty_printed_signature(True), 'fn(a, b=1)\n'
    '  Args:\n'
    '    a: float32 Tensor, shape=<unknown>\n'
    '  Returns:\n'
    '    float32 Tensor, shape=<unknown>')
