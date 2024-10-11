# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# Gh#34708
df = DataFrame({"x": [1, 2, np.NaN], "y": [3.0, 4, np.NaN]})
df2 = df[["x"]]
df2["y"] = df["y"]
if not using_array_manager:
    assert len(df2._mgr.blocks) == 2

res = df2.unstack()
expected = df.unstack()
tm.assert_series_equal(res, expected)
