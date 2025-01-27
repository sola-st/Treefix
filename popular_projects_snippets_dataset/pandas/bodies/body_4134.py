# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
# GH#12222
df = DataFrame(
    {
        "a": [datetime.datetime(2015, 1, 1)],
        "b": [None],
        "c": [None],
        "d": [""],
        "e": [[]],
        "f": [set()],
        "g": [{}],
    }
)
expected = Series(
    [datetime.datetime(2015, 1, 1), None, None, "", [], set(), {}],
    index=list("abcdefg"),
    name=0,
    dtype="object",
)
_, result = next(df.iterrows())
tm.assert_series_equal(result, expected)
