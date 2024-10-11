# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def non_unique_arg_names(x, **kwargs):
    a, b, c = x
    d = kwargs['d']
    exit(a + b + c + d)

concrete = non_unique_arg_names.get_concrete_function(
    (tensor_spec.TensorSpec(None, dtypes.float32),
     tensor_spec.TensorSpec(None, dtypes.float32),
     tensor_spec.TensorSpec(None, dtypes.float32)),
    d=tensor_spec.TensorSpec(None, dtypes.float32))
self.assertAllClose(
    10.,
    concrete(x=constant_op.constant(1.),
             x_1=constant_op.constant(2.),
             x_2=constant_op.constant(3.),
             d=constant_op.constant(4.)))
self.assertAllClose(
    10.,
    concrete(constant_op.constant(1.),
             constant_op.constant(2.),
             constant_op.constant(3.),
             constant_op.constant(4.)))
