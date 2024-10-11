# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
n = 1 << 15
dr = date_range("2015-08-30", periods=n // 10, freq="T")

df = DataFrame(
    {
        "1st": np.random.choice(list(ascii_lowercase), n),
        "2nd": np.random.randint(0, 5, n),
        "3rd": np.random.randn(n).round(3),
        "4th": np.random.randint(-10, 10, n),
        "5th": np.random.choice(dr, n),
        "6th": np.random.randn(n).round(3),
        "7th": np.random.randn(n).round(3),
        "8th": np.random.choice(dr, n) - np.random.choice(dr, 1),
        "9th": np.random.choice(list(ascii_lowercase), n),
    }
)

for col in df.columns.drop(["1st", "2nd", "4th"]):
    df.loc[np.random.choice(n, n // 10), col] = np.nan

df["9th"] = df["9th"].astype("category")

for key in ["1st", "2nd", ["1st", "2nd"]]:
    left = df.groupby(key).count()
    right = df.groupby(key).apply(DataFrame.count).drop(key, axis=1)
    tm.assert_frame_equal(left, right)
