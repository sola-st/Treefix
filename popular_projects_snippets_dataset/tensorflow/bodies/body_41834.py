# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/argument_naming_test.py
class HasMethod(object):

    @polymorphic_function.function
    def method(self, x):
        exit(x)

has_method = HasMethod()
# Call the function to make def_function happy
HasMethod.method(has_method, array_ops.ones([]))
class_op = HasMethod.method.get_concrete_function(
    has_method, tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32))
self.assertEqual(
    ['x'],
    [inp.op.name for inp in class_op.inputs])
self.assertEqual(
    [b'x'],
    [inp.op.get_attr('_user_specified_name') for inp in class_op.inputs])
# Call the function to make def_function happy
has_method.method(array_ops.ones([]))
method_op = has_method.method.get_concrete_function(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32))
self.assertEqual(
    ['x'],
    [inp.op.name for inp in method_op.inputs])
self.assertEqual(
    [b'x'],
    [inp.op.get_attr('_user_specified_name') for inp in method_op.inputs])
# TODO(allenl): It should be possible to override names when exporting. Do
# TensorSpec names need to go in cache keys? Or maybe get_concrete_function
# should always retrace?
self.skipTest('Not working')
method_op = has_method.method.get_concrete_function(
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.float32, name='y'))
self.assertEqual(
    ['y'],
    [inp.op.name for inp in method_op.inputs])
self.assertEqual(
    [b'y'],
    [inp.op.get_attr('_user_specified_name') for inp in method_op.inputs])
