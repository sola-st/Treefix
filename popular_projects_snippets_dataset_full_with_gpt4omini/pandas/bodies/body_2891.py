# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_combine_first.py
# GH 7509 (not fixed)
dfa = DataFrame([[pd.Timestamp("2011-01-01"), 2]], columns=["a", "b"])
dfb = DataFrame([[4], [5]], columns=["b"])
assert dfa["a"].dtype == "datetime64[ns]"
assert dfa["b"].dtype == "int64"

res = dfa.combine_first(dfb)
exp = DataFrame(
    {"a": [pd.Timestamp("2011-01-01"), pd.NaT], "b": [2, 5]},
    columns=["a", "b"],
)
tm.assert_frame_equal(res, exp)
assert res["a"].dtype == "datetime64[ns]"
# TODO: this must be int64
assert res["b"].dtype == "int64"

res = dfa.iloc[:0].combine_first(dfb)
exp = DataFrame({"a": [np.nan, np.nan], "b": [4, 5]}, columns=["a", "b"])
tm.assert_frame_equal(res, exp)
# TODO: this must be datetime64
assert res["a"].dtype == "float64"
# TODO: this must be int64
assert res["b"].dtype == "int64"
