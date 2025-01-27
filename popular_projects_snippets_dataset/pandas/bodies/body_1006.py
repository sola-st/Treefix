# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py

# GH 7106
# non-unique mi index support
df = (
    DataFrame(
        {
            "A": ["foo", "foo", "foo", "foo"],
            "B": ["a", "a", "a", "a"],
            "C": [1, 2, 1, 3],
            "D": [1, 2, 3, 4],
        }
    )
    .set_index(["A", "B", "C"])
    .sort_index()
)
assert not df.index.is_unique
expected = (
    DataFrame({"A": ["foo", "foo"], "B": ["a", "a"], "C": [1, 1], "D": [1, 3]})
    .set_index(["A", "B", "C"])
    .sort_index()
)
result = df.loc[(slice(None), slice(None), 1), :]
tm.assert_frame_equal(result, expected)

# this is equivalent of an xs expression
result = df.xs(1, level=2, drop_level=False)
tm.assert_frame_equal(result, expected)

df = (
    DataFrame(
        {
            "A": ["foo", "foo", "foo", "foo"],
            "B": ["a", "a", "a", "a"],
            "C": [1, 2, 1, 2],
            "D": [1, 2, 3, 4],
        }
    )
    .set_index(["A", "B", "C"])
    .sort_index()
)
assert not df.index.is_unique
expected = (
    DataFrame({"A": ["foo", "foo"], "B": ["a", "a"], "C": [1, 1], "D": [1, 3]})
    .set_index(["A", "B", "C"])
    .sort_index()
)
result = df.loc[(slice(None), slice(None), 1), :]
assert not result.index.is_unique
tm.assert_frame_equal(result, expected)

# GH12896
# numpy-implementation dependent bug
ints = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    12,
    13,
    14,
    14,
    16,
    17,
    18,
    19,
    200000,
    200000,
]
n = len(ints)
idx = MultiIndex.from_arrays([["a"] * n, ints])
result = Series([1] * n, index=idx)
result = result.sort_index()
result = result.loc[(slice(None), slice(100000))]
expected = Series([1] * (n - 2), index=idx[:-2]).sort_index()
tm.assert_series_equal(result, expected)
