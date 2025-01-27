# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval([[[{"a": 5}]]])
with self.assertRaisesRegex(
    ValueError, r"Expected outer_axis \(2\) to be less than "
    r"or equal to inner_axis \(1\)"):
    st.merge_dims(2, 1)
