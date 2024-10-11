# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""See b/183245576."""
st = structured_tensor.StructuredTensor.from_pyval([{}])
self.assertAllEqual([1], st.shape.as_list())
