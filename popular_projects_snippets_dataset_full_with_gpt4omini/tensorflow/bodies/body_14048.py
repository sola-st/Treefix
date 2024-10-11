# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
"""See b/179195750."""
st = structured_tensor.StructuredTensor.from_pyval([{
    "foo": [{
        "bar": [{
            "baz": [b"FW"]
        }]
    }]
}])
st2 = st.field_value(("foo", "bar"))
self.assertLen(st2.row_partitions, st2.rank - 1)
