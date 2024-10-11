# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
x = ops.convert_to_tensor([1, 2, 3])
y = ops.convert_to_tensor([1.0, 2.0])
spec1 = TwoTensorsSpec([100], x.dtype, y.shape, y.dtype, "green")
spec2 = TwoTensorsSpec(x.shape, x.dtype, y.shape, dtypes.bool, "green")
with self.assertRaises(ValueError):
    spec1._from_tensor_list([x, y])  # shape mismatch
with self.assertRaises(ValueError):
    spec2._from_tensor_list([x, y])  # dtype mismatch
