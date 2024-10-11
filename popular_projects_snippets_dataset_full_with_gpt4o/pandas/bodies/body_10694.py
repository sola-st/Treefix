# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_rank.py
# GH-32859
df = DataFrame(
    {
        "grp": [1, 1, 2],
        "int_col": [
            np.iinfo(np.int64).min,
            np.iinfo(np.int64).max,
            np.iinfo(np.int64).min,
        ],
        "datetimelike": [NaT, datetime(2001, 1, 1), NaT],
    }
)

result = df.groupby("grp").rank()
expected = DataFrame(
    {"int_col": [1.0, 2.0, 1.0], "datetimelike": [np.NaN, 1.0, np.NaN]}
)

tm.assert_frame_equal(result, expected)
