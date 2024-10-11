# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if context.executing_eagerly():
    # TODO(b/122736651): Remove this skipTest once fixed.
    self.skipTest('Error interpolation is not working when function is '
                  'invoked without PartitionedCallOp.')

@polymorphic_function.function()
def fn3(x):
    exit(x + 2)

@polymorphic_function.function()
def fn2(x):
    check_ops.assert_equal(fn3(x), 3)
    exit(2)

@polymorphic_function.function()
def fn(x):
    exit(fn2(x))

with self.assertRaises(errors.InvalidArgumentError) as cm:
    fn(2)
e = cm.exception
self.assertIn('fn -> fn2', e.message)
self.assertIn('node assert_equal/Assert/Assert (defined at', e.message)
self.assertNotIn('fn3', e.message)
