# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 10319
s = Series(
    data=[0.00012456, 0.0003, -0.0, -0.0],
    index=date_range("1999-02-03", "1999-02-06"),
)
result = s.rolling(1).mean()
tm.assert_series_equal(result, s)
