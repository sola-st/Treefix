# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
@quarantine.defun_with_attributes
def fn(x, z=(1., 2.), y=3.):
    z1, z2 = z
    exit({'alpha': x + y + z1, 'beta': x * y + z2})
# Call the function to make def_function happy
fn(array_ops.ones([]))

fn_op = fn.get_concrete_function(
    x=tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.float32),
    y=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32))
self.assertEqual(
    ['x', 'y'],
    [inp.op.name for inp in fn_op.inputs])
self.assertEqual(
    [b'x', b'y'],
    [inp.op.get_attr('_user_specified_name') for inp in fn_op.inputs])
self.assertEqual({'alpha', 'beta'},
                 set(fn_op.graph.structured_outputs.keys()))

fn_op2 = fn.get_concrete_function(
    z=(tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.float32,
                              name='z_first'),
       tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32,
                              name='z_second')),
    y=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='custom'),
    x=4.)
self.assertEqual(
    ['z_first', 'z_second', 'custom'],
    [inp.op.name for inp in fn_op2.inputs])
self.assertEqual(
    [b'z_first', b'z_second', b'custom'],
    [inp.op.get_attr('_user_specified_name') for inp in fn_op2.inputs])

fn_op3 = fn.get_concrete_function(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='custom'),
    z=(tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.float32,
                              name='z1'),
       tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='z2')),
    y=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32))
self.assertEqual(
    ['custom', 'z1', 'z2', 'y'],
    [inp.op.name for inp in fn_op3.inputs])
self.assertEqual(
    [b'custom', b'z1', b'z2', b'y'],
    [inp.op.get_attr('_user_specified_name') for inp in fn_op3.inputs])
