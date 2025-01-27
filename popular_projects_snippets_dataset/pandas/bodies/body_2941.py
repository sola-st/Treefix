# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {
        "A": [1, 2, np.nan, 4],
        "B": [1, 4, 9, np.nan],
        "C": [1, 2, 3, 5],
        "D": list("abcd"),
    }
)
expected = DataFrame(
    {
        "A": [1.0, 2.0, 3.0, 4.0],
        "B": [1.0, 4.0, 9.0, 9.0],
        "C": [1, 2, 3, 5],
        "D": list("abcd"),
    }
)
result = df.interpolate()
tm.assert_frame_equal(result, expected)

# check we didn't operate inplace GH#45791
cvalues = df["C"]._values
dvalues = df["D"].values
assert not np.shares_memory(cvalues, result["C"]._values)
assert not np.shares_memory(dvalues, result["D"]._values)

res = df.interpolate(inplace=True)
assert res is None
tm.assert_frame_equal(df, expected)

# check we DID operate inplace
assert np.shares_memory(df["C"]._values, cvalues)
assert np.shares_memory(df["D"]._values, dvalues)
