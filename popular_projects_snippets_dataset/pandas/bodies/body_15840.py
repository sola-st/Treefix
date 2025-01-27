# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#36984 if the user explicitly passes value=None, give it to them
ser = pd.Series([0, 0, ""], dtype=object)
result = ser.replace("", None)
expected = pd.Series([0, 0, None], dtype=object)
tm.assert_series_equal(result, expected)

# Cast column 2 to object to avoid implicit cast when setting entry to ""
df = pd.DataFrame(np.zeros((3, 3))).astype({2: object})
df.iloc[2, 2] = ""
result = df.replace("", None)
expected = pd.DataFrame(
    {
        0: np.zeros(3),
        1: np.zeros(3),
        2: np.array([0.0, 0.0, None], dtype=object),
    }
)
assert expected.iloc[2, 2] is None
tm.assert_frame_equal(result, expected)

# GH#19998 same thing with object dtype
ser = pd.Series([10, 20, 30, "a", "a", "b", "a"])
result = ser.replace("a", None)
expected = pd.Series([10, 20, 30, None, None, "b", None])
assert expected.iloc[-1] is None
tm.assert_series_equal(result, expected)
