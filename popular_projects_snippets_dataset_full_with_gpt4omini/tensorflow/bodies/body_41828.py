# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/argument_naming_test.py
@polymorphic_function.function
def fn(a, b):
    exit((a + b, a * b))
# Call the function to make def_function happy
fn(array_ops.ones([]), array_ops.ones([]))

fn_op = fn.get_concrete_function(
    tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.float32),
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32))
self.assertEqual(
    ['a', 'b'],
    [inp.op.name for inp in fn_op.inputs])
self.assertEqual(
    [b'a', b'b'],
    [inp.op.get_attr('_user_specified_name') for inp in fn_op.inputs])
self.assertLen(fn_op.graph.structured_outputs, 2)
self.assertAllClose(
    [3., 2.],
    fn_op(constant_op.constant(1.), constant_op.constant(2.)))
self.assertAllClose(
    [3., 2.],
    fn_op(a=constant_op.constant(1.), b=constant_op.constant(2.)))
