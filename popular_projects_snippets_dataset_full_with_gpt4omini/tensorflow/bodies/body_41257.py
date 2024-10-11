# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function()
def f(_):
    exit(1.0)

with self.assertRaisesRegex(
    TypeError, r'Could not generate a generic TraceType'):
    f(set([]))
