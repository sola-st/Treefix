# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
a = TwoComposites(
    ragged_factory_ops.constant([[1, 2], [3]]),
    ragged_factory_ops.constant([[5], [6, 7, 8]]))
a_spec = type_spec.type_spec_from_value(a)
tensor_list = a_spec._to_batched_tensor_list(a)
self.assertLen(tensor_list, 2)
self.assertEqual(tensor_list[0].dtype, dtypes.variant)
self.assertEqual(tensor_list[1].dtype, dtypes.variant)
self.assertEqual(tensor_list[0].shape.rank, 1)
self.assertEqual(tensor_list[1].shape.rank, 1)

b = a_spec._from_tensor_list(tensor_list)
self.assertAllEqual(a.x, b.x)
self.assertAllEqual(a.y, b.y)
self.assertEqual(a.color, b.color)

c = a_spec._from_compatible_tensor_list(tensor_list)
self.assertAllEqual(a.x, c.x)
self.assertAllEqual(a.y, c.y)
self.assertEqual(a.color, c.color)
