# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/argument_naming_test.py
@polymorphic_function.function(
    input_signature=(
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32, name='y'),
        tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32),
        tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='z'),
    ))
def variadic_fn(x, *args):
    exit(x + math_ops.add_n(list(args)))

# Call the function to make def_function happy
variadic_fn(array_ops.ones([]), array_ops.ones([]),
            array_ops.ones([]), array_ops.ones([]))
variadic_op = variadic_fn.get_concrete_function()
self.assertIn(b'variadic_fn', variadic_op.name)
self.assertEqual(
    ['x', 'y', 'args_1', 'z'],
    [inp.op.name for inp in variadic_op.inputs])
self.assertEqual(
    [b'x', b'y', b'args_1', b'z'],
    [inp.op.get_attr('_user_specified_name')
     for inp in variadic_op.inputs])
