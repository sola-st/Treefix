# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
length = 20
if test_data == "default":
    ser = Series(data=np.random.rand(length))
elif test_data == "duplicates":
    ser = Series(data=np.random.choice(3, length))
elif test_data == "nans":
    ser = Series(
        data=np.random.choice([1.0, 0.25, 0.75, np.nan, np.inf, -np.inf], length)
    )

expected = ser.rolling(window).apply(
    lambda x: x.rank(method=method, pct=pct, ascending=ascending).iloc[-1]
)
result = ser.rolling(window).rank(method=method, pct=pct, ascending=ascending)

tm.assert_series_equal(result, expected)
