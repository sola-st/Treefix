# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""See b/183245576."""
st = structured_tensor.StructuredTensor.from_pyval([[{
    "a": {},
    "b": [3, 4]
}, {
    "a": {},
    "b": [5]
}], [{
    "a": {},
    "b": [7, 8, 9]
}]])
self.assertAllEqual(2, st.rank)
self.assertEqual(2, st.shape[0])
self.assertEmpty(st.field_value("a").field_names())
