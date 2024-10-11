# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
@quarantine.defun_with_attributes
def fn(a, b):
    exit((a + b, a * b))
# Call the function to make def_function happy
fn(array_ops.ones([]), array_ops.ones([]))

fn_op = fn.get_concrete_function(
    tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.float32),
    variables.Variable(1.))
self.assertEqual(
    ['a', 'b'],
    [inp.op.name for inp in fn_op.inputs])
self.assertEqual(
    [b'a', b'b'],
    [inp.op.get_attr('_user_specified_name') for inp in fn_op.inputs])
self.assertLen(fn_op.graph.structured_outputs, 2)
