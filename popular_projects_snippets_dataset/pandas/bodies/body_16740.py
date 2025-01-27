# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 16767
# non-duplicates should work with multiple categories
m = 5
df = DataFrame(
    {
        "a": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] * m,
        "b": ["t", "w", "x", "y", "z"] * 2 * m,
        "c": [
            letter
            for each in ["m", "n", "u", "p", "o"]
            for letter in [each] * 2 * m
        ],
        "d": [
            letter
            for each in [
                "aa",
                "bb",
                "cc",
                "dd",
                "ee",
                "ff",
                "gg",
                "hh",
                "ii",
                "jj",
            ]
            for letter in [each] * m
        ],
    }
)

# change them all to categorical variables
df = df.apply(lambda x: x.astype("category"))

# self-join should equal ourselves
result = merge(df, df, on=list(df.columns))

tm.assert_frame_equal(result, df)
