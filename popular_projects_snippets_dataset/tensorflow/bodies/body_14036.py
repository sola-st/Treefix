# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_fields(
    {
        "a":
            StructuredTensor.from_fields(
                {"b": [[[1, 11], [2, 12]], [[3, 13], [4, 14]]]},
                shape=[2, 2, 2])
    },
    shape=[2])
result = st.promote(("a", "b"), "new_field")
self.assertEqual(st.rank, 1)
self.assertEqual(st.field_value("a").rank, 3)
self.assertAllEqual(
    result.field_value("new_field"), [[1, 11, 2, 12], [3, 13, 4, 14]])
