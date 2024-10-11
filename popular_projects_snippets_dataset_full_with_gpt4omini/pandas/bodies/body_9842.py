# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 11704, 40373
df = DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "B": [4, 5, 6, 7, 8],
        "C": date_range(start="2016-01-01", periods=5, freq="D"),
    }
)

expected = [
    DataFrame(values, index=df.loc[index, "C"]) for (values, index) in expected
]
for (expected, actual) in zip(expected, df.rolling(window, on="C")):
    tm.assert_frame_equal(actual, expected)
