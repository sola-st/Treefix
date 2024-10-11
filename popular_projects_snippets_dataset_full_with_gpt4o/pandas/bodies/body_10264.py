# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH#37501
obj = frame_or_series(data, dtype=object)
result = obj.groupby([1] * len(data)).agg(bool_agg_func)
expected = frame_or_series([expected_res], index=np.array([1]), dtype="bool")
tm.assert_equal(result, expected)
