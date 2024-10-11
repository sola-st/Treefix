# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {
        "A": [1.0, 2.0, np.nan, 4.0],
        "B": [1, 4, 9, np.nan],
        "C": [1, 2, 3, 5],
        "D": list("abcd"),
    }
)

result = df["A"].interpolate()
expected = Series([1.0, 2.0, 3.0, 4.0], name="A")
tm.assert_series_equal(result, expected)

result = df["A"].interpolate(downcast="infer")
expected = Series([1, 2, 3, 4], name="A")
tm.assert_series_equal(result, expected)
