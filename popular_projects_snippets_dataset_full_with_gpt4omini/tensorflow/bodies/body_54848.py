# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
x = ops.convert_to_tensor([1, 2, 3])
y = ops.convert_to_tensor([1.0, 2.0])
color = "green"
spec = TwoTensorsSpec(x.shape, x.dtype, y.shape, y.dtype, color)
value = spec._from_tensor_list([x, y])
self.assertIs(value.x, x)
self.assertIs(value.y, y)
self.assertEqual(value.color, color)
