# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH 15118
# no match found - `where` value before earliest date in index
N = 10
df = date_range_frame.iloc[:N].copy()

result = df.asof("1989-12-31")

expected = Series(
    index=["A", "B"], name=Timestamp("1989-12-31"), dtype=np.float64
)
tm.assert_series_equal(result, expected)

result = df.asof(to_datetime(["1989-12-31"]))
expected = DataFrame(
    index=to_datetime(["1989-12-31"]), columns=["A", "B"], dtype="float64"
)
tm.assert_frame_equal(result, expected)

# Check that we handle PeriodIndex correctly, dont end up with
#  period.ordinal for series name
df = df.to_period("D")
result = df.asof("1989-12-31")
assert isinstance(result.name, Period)
