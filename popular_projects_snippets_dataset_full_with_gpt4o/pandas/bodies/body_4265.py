# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 19611
dti = pd.date_range("2016-01-01", periods=3)
ser = Series(["1 Day", "NaT", "2 Days"], dtype="timedelta64[ns]")
df = DataFrame({"A": dti, "B": ser})
other = DataFrame({"A": ser, "B": ser})
fill = pd.Timedelta(days=1).to_timedelta64()
result = df.add(other, fill_value=fill)

expected = DataFrame(
    {
        "A": Series(
            ["2016-01-02", "2016-01-03", "2016-01-05"], dtype="datetime64[ns]"
        ),
        "B": ser * 2,
    }
)
tm.assert_frame_equal(result, expected)
