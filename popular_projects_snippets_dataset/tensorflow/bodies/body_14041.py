# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_pyval(pyval)
updated_st = st.with_updates(updates, validate=False)
for key, value in updates.items():
    got = updated_st.field_value(key)
    self.assertAllEqual(
        value, got,
        "Update failed: key={}, value={}, got={}".format(key, value, got))
