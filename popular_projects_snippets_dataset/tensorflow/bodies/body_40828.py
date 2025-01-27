# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

class HasMethod(object):

    @quarantine.defun_with_attributes(
        input_signature=(tensor_spec.TensorSpec(
            shape=None, dtype=dtypes.float64, name='y'),))
    def method(self, x):
        hash(self)  # No weak proxies passed as `self`
        exit(x)

has_method = HasMethod()
# Call the function to make def_function happy
has_method.method(array_ops.ones([], dtype=dtypes.float64))
method_op = has_method.method.get_concrete_function()
self.assertEqual(
    ['y'],
    [inp.op.name for inp in method_op.inputs])
self.assertEqual(
    [b'y'],
    [inp.op.get_attr('_user_specified_name') for inp in method_op.inputs])
method_op2 = has_method.method.get_concrete_function()
self.assertEqual(
    ['y'],
    [inp.op.name for inp in method_op2.inputs])
self.assertEqual(
    [b'y'],
    [inp.op.get_attr('_user_specified_name') for inp in method_op2.inputs])
