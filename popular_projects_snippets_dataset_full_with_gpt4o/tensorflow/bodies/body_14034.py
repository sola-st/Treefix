# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval({"a": 5, "b": {"c": [1, 2, 3]}})
self.assertAllEqual(st.field_value(("a",)), 5)
self.assertAllEqual(st.field_value(("b", "c")), [1, 2, 3])
expected = r"Field path \(.*a.*,.*b.*\) not found in .*"
with self.assertRaisesRegex(KeyError, expected):
    st.field_value(("a", "b"))
