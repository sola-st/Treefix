# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = structured_tensor.StructuredTensor.from_pyval({"a": 5})
if not context.executing_eagerly():
    with self.assertRaisesRegex(ValueError, "only supported in eager mode."):
        st.to_pyval()
