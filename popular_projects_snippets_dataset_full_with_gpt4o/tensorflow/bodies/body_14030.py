# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval(st)
result = st.merge_dims(outer_axis, inner_axis)
self.assertAllEqual(result, expected)
