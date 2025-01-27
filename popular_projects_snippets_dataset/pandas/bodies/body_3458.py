# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# https://github.com/pandas-dev/pandas/issues/35606
idx = MultiIndex(
    levels=[[Timestamp("2020-07-20 00:00:00")], [3, 4]],
    codes=[[], []],
    names=["a", "b"],
)
df = DataFrame(index=idx, columns=["c", "d"])
result = df.reset_index()
expected = DataFrame(
    columns=list("abcd"), index=RangeIndex(start=0, stop=0, step=1)
)
expected["a"] = expected["a"].astype("datetime64[ns]")
expected["b"] = expected["b"].astype("int64")
tm.assert_frame_equal(result, expected)
