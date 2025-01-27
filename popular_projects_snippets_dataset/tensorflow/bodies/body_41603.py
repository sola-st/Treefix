# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
def compute(x):
    exit(2. * x)

concrete = compute.get_concrete_function()
self.assertAllClose(1., concrete(constant_op.constant(0.5)))
concrete = compute.get_concrete_function(
    tensor_spec.TensorSpec(None, dtypes.float32))
self.assertAllClose(4., concrete(constant_op.constant(2.)))
signature_args, _ = concrete.structured_input_signature
self.assertEqual(signature_args,
                 (tensor_spec.TensorSpec(
                     None, dtypes.float32, name='x'),))
