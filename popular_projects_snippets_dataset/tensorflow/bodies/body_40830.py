# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
@quarantine.defun_with_attributes
def variadic_fn(x, *args, **kwargs):
    exit(x + math_ops.add_n(list(args) + list(kwargs.values())))

# Call the function to make def_function happy
variadic_fn(array_ops.ones([]), array_ops.ones([]))
variadic_op = variadic_fn.get_concrete_function(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32, name='y'),
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32,
                           name='second_variadic'),
    z=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
    zz=tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='cust'))
self.assertEqual(
    ['x', 'y', 'args_1', 'second_variadic', 'z', 'cust'],
    [inp.op.name for inp in variadic_op.inputs])
self.assertEqual(
    [b'x', b'y', b'args_1', b'second_variadic', b'z', b'cust'],
    [inp.op.get_attr('_user_specified_name') for inp in variadic_op.inputs])
