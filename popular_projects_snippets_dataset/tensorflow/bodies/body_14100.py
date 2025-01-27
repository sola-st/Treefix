# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
if check_shape:
    self.assertEqual(repr(a.shape), repr(b.shape))
self.assertEqual(set(a.field_names()), set(b.field_names()))
for field in a.field_names():
    a_value = a.field_value(field)
    b_value = b.field_value(field)
    self.assertIs(type(a_value), type(b_value))
    if isinstance(a_value, structured_tensor.StructuredTensor):
        self._assertStructuredEqual(a_value, b_value, msg, check_shape)
    else:
        self.assertAllEqual(a_value, b_value, msg)
