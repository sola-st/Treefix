# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
pyval = {"a": 12, "b": {"c": 23, "d": {"e": 11}}}
st = StructuredTensor.from_pyval(pyval)
updated_st = st.with_updates({("b", "c"): None}, validate=True)
self.assertNotIn("c", updated_st.field_value("b").field_names())
with self.assertRaisesRegex(ValueError,
                            r"cannot delete.*\('b', 'x'\).*not present"):
    st.with_updates({("b", "x"): None}, validate=True)
with self.assertRaisesRegex(ValueError,
                            r"cannot delete.*\'x'.*not present"):
    st.with_updates({"x": None}, validate=False)

# Test that nrows() and rowpartitions() is preserved after removal.
pyval = [[{"a": 1}, {"a": 2}], [{"a": 3}]]
st = StructuredTensor.from_pyval(pyval)
self.assertLen(st.row_partitions, 1)
self.assertAllEqual(st.nrows(), 2)
self.assertAllEqual(st.row_partitions[0].row_lengths(), [2, 1])
updated_st = st.with_updates({("a",): None}, validate=True)
self.assertLen(updated_st.row_partitions, 1)
self.assertAllEqual(updated_st.nrows(), 2)
self.assertAllEqual(updated_st.row_partitions[0].row_lengths(), [2, 1])

# Test that it works also for rank-1 and rank-0 empty results.
pyval = [{"a": 1}, {"a": 2}]
st = StructuredTensor.from_pyval(pyval)
self.assertEqual(st.rank, 1)
updated_st = st.with_updates({("a",): None}, validate=True)
self.assertEqual(updated_st.rank, 1)

# assertEqual won't work because nrows() returns a tensor, and
# assertEqual doesn't do the magic to convert them to numbers in a
# way that works in eager/non-eager mode.
self.assertAllEqual(updated_st.nrows(), 2)
pyval = {"a": [0, 1]}
st = StructuredTensor.from_pyval(pyval)
self.assertEqual(st.rank, 0)
updated_st = st.with_updates({("a",): None}, validate=True)
self.assertEqual(updated_st.rank, 0)
self.assertFalse(updated_st.row_partitions)
self.assertIsNone(updated_st.nrows())
