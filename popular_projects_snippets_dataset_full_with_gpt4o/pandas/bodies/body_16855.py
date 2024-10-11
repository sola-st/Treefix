# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
s_list = list("abc")
s_series = Series(s_list)
s_series_index = Series(s_list, list("ABC"))

expected = DataFrame(
    {"a": [1, 0, 0], "b": [0, 1, 0], "c": [0, 0, 1]},
    dtype=self.effective_dtype(dtype),
)
if sparse:
    expected = expected.apply(SparseArray, fill_value=0.0)
result = get_dummies(s_list, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)

result = get_dummies(s_series, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)

expected.index = list("ABC")
result = get_dummies(s_series_index, sparse=sparse, dtype=dtype)
tm.assert_frame_equal(result, expected)
