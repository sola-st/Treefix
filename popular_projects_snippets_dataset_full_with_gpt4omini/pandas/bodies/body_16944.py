# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# https://github.com/pandas-dev/pandas/issues/11058
idx = Index(
    [dt.date(2013, 1, 1), dt.date(2014, 1, 1), dt.date(2015, 1, 1)],
    dtype="object",
)

s = Series(
    ["a", "b"],
    index=MultiIndex.from_arrays(
        [
            [1, 2],
            idx[:-1],
        ],
        names=["first", "second"],
    ),
)
s2 = Series(
    ["a", "b"],
    index=MultiIndex.from_arrays(
        [[1, 2], idx[::2]],
        names=["first", "second"],
    ),
)
mi = MultiIndex.from_arrays(
    [[1, 2, 2], idx],
    names=["first", "second"],
)
assert mi.levels[1].dtype == object

expected = DataFrame(
    [["a", "a"], ["b", np.nan], [np.nan, "b"]],
    index=mi,
)
result = concat([s, s2], axis=1)
tm.assert_frame_equal(result, expected)
