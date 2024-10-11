# Extracted from ./data/repos/pandas/pandas/tests/plotting/conftest.py
n = 100
with tm.RNGContext(42):
    gender = np.random.choice(["Male", "Female"], size=n)
    classroom = np.random.choice(["A", "B", "C"], size=n)

    hist_df = DataFrame(
        {
            "gender": gender,
            "classroom": classroom,
            "height": np.random.normal(66, 4, size=n),
            "weight": np.random.normal(161, 32, size=n),
            "category": np.random.randint(4, size=n),
            "datetime": to_datetime(
                np.random.randint(
                    812419200000000000,
                    819331200000000000,
                    size=n,
                    dtype=np.int64,
                )
            ),
        }
    )
exit(hist_df)
