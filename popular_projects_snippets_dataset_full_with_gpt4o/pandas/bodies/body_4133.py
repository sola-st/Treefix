# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
# GH#19671
s = DataFrame(
    {
        "non_iso8601": ["M1701", "M1802", "M1903", "M2004"],
        "iso8601": date_range("2000-01-01", periods=4, freq="M"),
    }
)
for k, v in s.iterrows():
    exp = s.loc[k]
    tm.assert_series_equal(v, exp)
