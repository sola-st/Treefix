# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH#40585
obj = frame_or_series([pd.NA, 1], dtype=dtype)
expected_res = True
if not skipna and bool_agg_func == "all":
    expected_res = pd.NA
expected = frame_or_series([expected_res], index=np.array([1]), dtype="boolean")

result = obj.groupby([1, 1]).agg(bool_agg_func, skipna=skipna)
tm.assert_equal(result, expected)
