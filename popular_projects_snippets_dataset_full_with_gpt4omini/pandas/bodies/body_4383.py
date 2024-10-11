# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
datetime_series = tm.makeTimeSeries(nper=30)
# test expects index shifted by 5
datetime_series_short = tm.makeTimeSeries(nper=30)[5:]

frame = DataFrame({"col1": datetime_series, "col2": datetime_series_short})

# col2 is padded with NaN
assert len(datetime_series) == 30
assert len(datetime_series_short) == 25

tm.assert_series_equal(frame["col1"], datetime_series.rename("col1"))

exp = Series(
    np.concatenate([[np.nan] * 5, datetime_series_short.values]),
    index=datetime_series.index,
    name="col2",
)
tm.assert_series_equal(exp, frame["col2"])

frame = DataFrame(
    {"col1": datetime_series, "col2": datetime_series_short},
    columns=["col2", "col3", "col4"],
)

assert len(frame) == len(datetime_series_short)
assert "col1" not in frame
assert isna(frame["col3"]).all()

# Corner cases
assert len(DataFrame()) == 0

# mix dict and array, wrong size - no spec for which error should raise
# first
msg = "Mixing dicts with non-Series may lead to ambiguous ordering."
with pytest.raises(ValueError, match=msg):
    DataFrame({"A": {"a": "a", "b": "b"}, "B": ["a", "b", "c"]})
