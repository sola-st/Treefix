# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH 7227
df = DataFrame({"A": dates, "B": np.arange(len(dates))})
result = df.set_index("A").resample("M").count()
exp_idx = DatetimeIndex(
    ["2014-07-31", "2014-08-31", "2014-09-30", "2014-10-31", "2014-11-30"],
    freq="M",
    name="A",
)
expected = DataFrame({"B": [1, 0, 2, 2, 1]}, index=exp_idx)
if df["A"].isna().any():
    expected.index = expected.index._with_freq(None)
tm.assert_frame_equal(result, expected)

result = df.groupby(Grouper(freq="M", key="A")).count()
tm.assert_frame_equal(result, expected)

df = DataFrame({"A": dates, "B": np.arange(len(dates)), "C": np.arange(len(dates))})
result = df.set_index("A").resample("M").count()
expected = DataFrame(
    {"B": [1, 0, 2, 2, 1], "C": [1, 0, 2, 2, 1]},
    index=exp_idx,
    columns=["B", "C"],
)
if df["A"].isna().any():
    expected.index = expected.index._with_freq(None)
tm.assert_frame_equal(result, expected)

result = df.groupby(Grouper(freq="M", key="A")).count()
tm.assert_frame_equal(result, expected)
