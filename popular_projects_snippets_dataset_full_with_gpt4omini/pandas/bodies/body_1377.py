# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# GH#20511
df = DataFrame({"A": ["2022-01-01", "2022-01-02"], "B": ["2021", "2022"]})

df.iloc[:, [0]] = DataFrame({"A": to_datetime(["2021", "2022"])})
expected = DataFrame(
    {
        "A": [
            Timestamp("2021-01-01 00:00:00"),
            Timestamp("2022-01-01 00:00:00"),
        ],
        "B": ["2021", "2022"],
    }
)
tm.assert_frame_equal(df, expected, check_dtype=False)
