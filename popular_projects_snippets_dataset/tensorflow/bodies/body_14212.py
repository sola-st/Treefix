# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
if not (isinstance(a, structured_tensor.StructuredTensor) or
        isinstance(b, structured_tensor.StructuredTensor)):
    super(StructuredTensorSliceTest, self).assertAllEqual(a, b, msg)
elif (isinstance(a, structured_tensor.StructuredTensor) and
      isinstance(b, structured_tensor.StructuredTensor)):
    a_shape = tensor_shape.as_shape(a.shape)
    b_shape = tensor_shape.as_shape(b.shape)
    a_shape.assert_is_compatible_with(b_shape)
    self.assertEqual(set(a.field_names()), set(b.field_names()))
    for field in a.field_names():
        self.assertAllEqual(a.field_value(field), b.field_value(field))
elif isinstance(b, structured_tensor.StructuredTensor):
    self.assertAllEqual(b, a, msg)
else:
    if a.rank == 0:
        self.assertIsInstance(b, dict)
        self.assertEqual(set(a.field_names()), set(b))
        for (key, b_val) in b.items():
            a_val = a.field_value(key)
            self.assertAllEqual(a_val, b_val)
    else:
        self.assertIsInstance(b, (list, tuple))
        a.shape[:1].assert_is_compatible_with([len(b)])
        for i in range(len(b)):
            self.assertAllEqual(a[i], b[i])
