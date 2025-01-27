# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""Test a field with its own row_partition. See b/179195750."""
st = structured_tensor.StructuredTensor.from_pyval([[[{"baz": [b"FW"]}]]])
self.assertLen(st.row_partitions, st.rank - 1)
st2 = structured_tensor.StructuredTensor.from_fields(
    fields={"bar": st}, shape=(None, None), validate=False)
st3 = st2.field_value("bar")
self.assertLen(st3.row_partitions, st3.rank - 1)
