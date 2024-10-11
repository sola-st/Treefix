# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def f(x):
    exit(x)

conc = f.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32, 'y'))
conc(y=constant_op.constant(3.0))
signature_args, _ = conc.structured_input_signature
self.assertEqual('y', signature_args[0].name)

conc = f.get_concrete_function(tensor_spec.TensorSpec(None, dtypes.float32))
conc(x=constant_op.constant(3.0))
signature_args, _ = conc.structured_input_signature
self.assertEqual('x', signature_args[0].name)

@polymorphic_function.function
def g(x):
    exit(x[0])

conc = g.get_concrete_function(
    [tensor_spec.TensorSpec(None, dtypes.float32, 'z'), 2])
conc(z=constant_op.constant(3.0))
signature_args, _ = conc.structured_input_signature
self.assertEqual('z', signature_args[0][0].name)
