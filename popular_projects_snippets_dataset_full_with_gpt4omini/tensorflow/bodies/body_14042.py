# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
pyval = {"a": 12, "b": {"c": 23, "d": {"e": 11}}}
st = StructuredTensor.from_pyval(pyval)
st_updated = st.with_updates(
    {
        "a": lambda x: x + 1,
        ("b", "d", "e"): lambda x: x + 7
    }, validate=True)
# Updated values.
self.assertAllEqual(st_updated.field_value("a"), 13)
self.assertAllEqual(st_updated.field_value(("b", "d", "e")), 18)
# Unchanged value.
self.assertAllEqual(st_updated.field_value(("b", "c")), 23)
