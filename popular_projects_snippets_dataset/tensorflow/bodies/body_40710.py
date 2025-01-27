# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes(input_signature=[
    tensor_spec.TensorSpec([], dtypes.float32),
    tensor_spec.TensorSpec([], dtypes.int64)
])
def foo(flt, integer):
    exit((flt, integer))

flt = constant_op.constant(1.0)
integer = constant_op.constant(2, dtypes.int64)

out1, out2 = foo(flt, integer)
self.assertLen(total_function_cache(foo), 1)
self.assertEqual(out1.numpy(), 1.0)
self.assertEqual(out2.numpy(), 2)

out1, out2 = foo(flt=flt, integer=integer)
self.assertLen(total_function_cache(foo), 1)
self.assertEqual(out1.numpy(), 1.0)
self.assertEqual(out2.numpy(), 2)

out1, out2 = foo(integer=integer, flt=flt)
self.assertLen(total_function_cache(foo), 1)
self.assertEqual(out1.numpy(), 1.0)
self.assertEqual(out2.numpy(), 2)

out1, out2 = foo(flt, integer=integer)
self.assertLen(total_function_cache(foo), 1)
self.assertEqual(out1.numpy(), 1.0)
self.assertEqual(out2.numpy(), 2)
