# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# multiple setting
df = DataFrame(
    {"A": ["foo", "bar", "baz"], "B": Series(range(3), dtype=np.int64)}
)
rhs = df.loc[1:2]
rhs.index = df.index[0:2]
df.loc[0:1] = rhs
expected = DataFrame(
    {"A": ["bar", "baz", "baz"], "B": Series([1, 2, 2], dtype=np.int64)}
)
tm.assert_frame_equal(df, expected)

# multiple setting with frame on rhs (with M8)
df = DataFrame(
    {
        "date": date_range("2000-01-01", "2000-01-5"),
        "val": Series(range(5), dtype=np.int64),
    }
)
expected = DataFrame(
    {
        "date": [
            Timestamp("20000101"),
            Timestamp("20000102"),
            Timestamp("20000101"),
            Timestamp("20000102"),
            Timestamp("20000103"),
        ],
        "val": Series([0, 1, 0, 1, 2], dtype=np.int64),
    }
)
rhs = df.loc[0:2]
rhs.index = df.index[2:5]
df.loc[2:4] = rhs
tm.assert_frame_equal(df, expected)
