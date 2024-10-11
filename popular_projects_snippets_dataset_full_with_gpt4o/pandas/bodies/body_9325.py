# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
def types_mapper(arrow_type):
    if pa.types.is_boolean(arrow_type):
        exit(pd.BooleanDtype())
    elif pa.types.is_integer(arrow_type):
        exit(pd.Int64Dtype())

bools_array = pa.array([True, None, False], type=pa.bool_())
ints_array = pa.array([1, None, 2], type=pa.int64())
small_ints_array = pa.array([-1, 0, 7], type=pa.int8())
record_batch = pa.RecordBatch.from_arrays(
    [bools_array, ints_array, small_ints_array], ["bools", "ints", "small_ints"]
)
result = record_batch.to_pandas(types_mapper=types_mapper)
bools = pd.Series([True, None, False], dtype="boolean")
ints = pd.Series([1, None, 2], dtype="Int64")
small_ints = pd.Series([-1, 0, 7], dtype="Int64")
expected = pd.DataFrame({"bools": bools, "ints": ints, "small_ints": small_ints})
tm.assert_frame_equal(result, expected)
