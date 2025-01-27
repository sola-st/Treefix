# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py

df = DataFrame(
    {
        "A": [12, 12, 19, 11],
        "B": [10, 10, np.nan, 3],
        "C": [1, np.nan, np.nan, np.nan],
        "D": [np.nan, np.nan, "a", np.nan],
        "E": Categorical([np.nan, np.nan, "a", np.nan]),
        "F": to_datetime(["NaT", "2000-1-2", "NaT", "NaT"]),
        "G": to_timedelta(["1 days", "nan", "nan", "nan"]),
        "H": [8, 8, 9, 9],
        "I": [9, 9, 8, 8],
        "J": [1, 1, np.nan, np.nan],
        "K": Categorical(["a", np.nan, "a", np.nan]),
        "L": to_datetime(["2000-1-2", "2000-1-2", "NaT", "NaT"]),
        "M": to_timedelta(["1 days", "nan", "1 days", "nan"]),
        "N": np.arange(4, dtype="int64"),
    }
)

result = df[sorted(expected.keys())].mode(dropna=dropna)
expected = DataFrame(expected)
tm.assert_frame_equal(result, expected)
