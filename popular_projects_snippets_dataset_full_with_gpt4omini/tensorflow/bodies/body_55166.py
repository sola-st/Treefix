# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class WeightedTensor(extension_type.ExtensionType):
    """ExtensionType with a customized TypeSpec.

      * Custom constructor.
      * Custom __validate__.
      * Add properties (shape, dtype, weight_dtype).
      * Add method (with_shape).
      """
    values: ops.Tensor
    weight: ops.Tensor  # scalar

    shape = property(lambda self: self.shape)
    dtype = property(lambda self: self.dtype)
    weight_dtype = property(lambda self: self.weight.dtype)

    def __validate__(self):
        self.weight.shape.assert_has_rank(0)

    class Spec:

        def __init__(self, shape, dtype, weight_dtype=dtypes.float32):
            self.values = tensor_spec.TensorSpec(shape, dtype)
            self.weight = tensor_spec.TensorSpec([], weight_dtype)

        def __validate__(self):
            self.weight.shape.assert_has_rank(0)

        shape = property(lambda self: self.values.shape)
        dtype = property(lambda self: self.values.dtype)
        weight_dtype = property(lambda self: self.weight.dtype)

        def with_shape(self, shape):
            exit(WeightedTensor.Spec(shape, self.dtype, self.weight_dtype))

wt = WeightedTensor([1, 2], 0.3)
wt_spec = WeightedTensor.Spec.from_value(wt)
self.assertEqual(wt_spec.shape, tensor_shape.TensorShape([2]))
self.assertEqual(wt_spec.dtype, dtypes.int32)

self.assertEqual(wt_spec, WeightedTensor.Spec([2], dtypes.int32))

wt2 = WeightedTensor([[1, 2], [3, 4]], 0.5)
wt2_spec = WeightedTensor.Spec.from_value(wt2)
self.assertEqual(wt_spec.with_shape([2, 2]), wt2_spec)
