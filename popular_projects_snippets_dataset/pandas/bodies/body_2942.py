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

result = df.set_index("C").interpolate()
expected = df.set_index("C")
expected.loc[3, "A"] = 3
expected.loc[5, "B"] = 9
tm.assert_frame_equal(result, expected)
