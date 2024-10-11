# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
zero = constant_op.constant(0)
spec = tensor_spec.TensorSpec.from_tensor(zero)
self.assertEqual(spec.dtype, dtypes.int32)
self.assertEqual(spec.shape, [])
# Tensor.name is meaningless when eager execution is enabled.
if not context.executing_eagerly():
    self.assertEqual(spec.name, "Const")
