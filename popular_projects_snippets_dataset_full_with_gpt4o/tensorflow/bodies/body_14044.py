# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""See b/183245576."""
st = structured_tensor.StructuredTensor.from_pyval([{}, {}, {}])
self.assertAllEqual([3], st.shape.as_list())
self.assertEmpty(st.field_names())
