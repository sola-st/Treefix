# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#14438
df1 = DataFrame(np.ones((2, 2)), columns=list("AB"))
df2 = DataFrame(np.ones((3, 2)) * 2, columns=list("AB"))
results = concat((df1, df2), keys=[("bee", "bah"), ("bee", "boo")])
expected = DataFrame(
    {
        "A": {
            ("bee", "bah", 0): 1.0,
            ("bee", "bah", 1): 1.0,
            ("bee", "boo", 0): 2.0,
            ("bee", "boo", 1): 2.0,
            ("bee", "boo", 2): 2.0,
        },
        "B": {
            ("bee", "bah", 0): 1.0,
            ("bee", "bah", 1): 1.0,
            ("bee", "boo", 0): 2.0,
            ("bee", "boo", 1): 2.0,
            ("bee", "boo", 2): 2.0,
        },
    }
)
tm.assert_frame_equal(results, expected)
