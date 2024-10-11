# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
# GH 10531
s_list = list("abc")
s_series = Series(s_list)
s_df = DataFrame(
    {"a": [0, 1, 0, 1, 2], "b": ["A", "A", "B", "C", "C"], "c": [2, 3, 3, 3, 2]}
)

expected = DataFrame(
    {"a": [1, 0, 0], "b": [0, 1, 0], "c": [0, 0, 1]},
    dtype=self.effective_dtype(dtype),
    columns=list("abc"),
)
if sparse:
    if is_integer_dtype(dtype):
        fill_value = 0
    elif dtype == bool:
        fill_value = False
    else:
        fill_value = 0.0

    expected = expected.apply(SparseArray, fill_value=fill_value)
result = get_dummies(s_list, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)

result = get_dummies(s_series, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)

result = get_dummies(s_df, columns=s_df.columns, sparse=sparse, dtype=dtype)
if sparse:
    dtype_name = f"Sparse[{self.effective_dtype(dtype).name}, {fill_value}]"
else:
    dtype_name = self.effective_dtype(dtype).name

expected = Series({dtype_name: 8})
result = result.dtypes.value_counts()
result.index = [str(i) for i in result.index]
tm.assert_series_equal(result, expected)

result = get_dummies(s_df, columns=["a"], sparse=sparse, dtype=dtype)

expected_counts = {"int64": 1, "object": 1}
expected_counts[dtype_name] = 3 + expected_counts.get(dtype_name, 0)

expected = Series(expected_counts).sort_index()
result = result.dtypes.value_counts()
result.index = [str(i) for i in result.index]
result = result.sort_index()
tm.assert_series_equal(result, expected)
