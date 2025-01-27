# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame(
    {
        "A": date_range("2012-1-1", periods=3, freq="D"),
        "B": date_range("2012-1-2", periods=3, freq="D"),
        "C": Timestamp("20120101") - timedelta(minutes=5, seconds=5),
    }
)

diffs = DataFrame({"A": df["A"] - df["C"], "B": df["A"] - df["B"]})

# min
result = diffs.min()
assert result[0] == diffs.loc[0, "A"]
assert result[1] == diffs.loc[0, "B"]

result = diffs.min(axis=1)
assert (result == diffs.loc[0, "B"]).all()

# max
result = diffs.max()
assert result[0] == diffs.loc[2, "A"]
assert result[1] == diffs.loc[2, "B"]

result = diffs.max(axis=1)
assert (result == diffs["A"]).all()

# abs
result = diffs.abs()
result2 = abs(diffs)
expected = DataFrame({"A": df["A"] - df["C"], "B": df["B"] - df["A"]})
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)

# mixed frame
mixed = diffs.copy()
mixed["C"] = "foo"
mixed["D"] = 1
mixed["E"] = 1.0
mixed["F"] = Timestamp("20130101")

# results in an object array
result = mixed.min()
expected = Series(
    [
        pd.Timedelta(timedelta(seconds=5 * 60 + 5)),
        pd.Timedelta(timedelta(days=-1)),
        "foo",
        1,
        1.0,
        Timestamp("20130101"),
    ],
    index=mixed.columns,
)
tm.assert_series_equal(result, expected)

# excludes non-numeric
result = mixed.min(axis=1, numeric_only=True)
expected = Series([1, 1, 1.0], index=[0, 1, 2])
tm.assert_series_equal(result, expected)

# works when only those columns are selected
result = mixed[["A", "B"]].min(1)
expected = Series([timedelta(days=-1)] * 3)
tm.assert_series_equal(result, expected)

result = mixed[["A", "B"]].min()
expected = Series(
    [timedelta(seconds=5 * 60 + 5), timedelta(days=-1)], index=["A", "B"]
)
tm.assert_series_equal(result, expected)

# GH 3106
df = DataFrame(
    {
        "time": date_range("20130102", periods=5),
        "time2": date_range("20130105", periods=5),
    }
)
df["off1"] = df["time2"] - df["time"]
assert df["off1"].dtype == "timedelta64[ns]"

df["off2"] = df["time"] - df["time2"]
df._consolidate_inplace()
assert df["off1"].dtype == "timedelta64[ns]"
assert df["off2"].dtype == "timedelta64[ns]"
