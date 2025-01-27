# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def fn(unused_a, unused_b):
    exit(None)

x = constant_op.constant(1)
fn_op = fn.get_concrete_function(x, x)
self.assertEqual(fn_op.output_dtypes, None)
self.assertEqual(fn_op.output_shapes, None)
self.assertAllEqual(fn_op(x, x), None)
