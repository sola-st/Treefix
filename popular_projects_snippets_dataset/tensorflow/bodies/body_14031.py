# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval([[[{
    "x": 1
}, {
    "x": 2
}], [{
    "x": 3
}]], [[{
    "x": 4
}]]])
result = st.merge_dims(0, 1)
expected_shape = tensor_shape.TensorShape([3, None])
self.assertTrue(expected_shape.is_compatible_with(result.shape))
