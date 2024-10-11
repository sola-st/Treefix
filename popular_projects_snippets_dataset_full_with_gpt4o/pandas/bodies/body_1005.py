# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py

# GH6134
# example test case
ix = MultiIndex.from_product(
    [_mklbl("A", 5), _mklbl("B", 7), _mklbl("C", 4), _mklbl("D", 2)]
)
df = DataFrame(np.arange(len(ix.to_numpy())), index=ix)

result = df.loc[(slice("A1", "A3"), slice(None), ["C1", "C3"]), :]
expected = df.loc[
    [
        (
            a,
            b,
            c,
            d,
        )
        for a, b, c, d in df.index.values
        if a in ("A1", "A2", "A3") and c in ("C1", "C3")
    ]
]
tm.assert_frame_equal(result, expected)

expected = df.loc[
    [
        (
            a,
            b,
            c,
            d,
        )
        for a, b, c, d in df.index.values
        if a in ("A1", "A2", "A3") and c in ("C1", "C2", "C3")
    ]
]
result = df.loc[(slice("A1", "A3"), slice(None), slice("C1", "C3")), :]
tm.assert_frame_equal(result, expected)

# test multi-index slicing with per axis and per index controls
index = MultiIndex.from_tuples(
    [("A", 1), ("A", 2), ("A", 3), ("B", 1)], names=["one", "two"]
)
columns = MultiIndex.from_tuples(
    [("a", "foo"), ("a", "bar"), ("b", "foo"), ("b", "bah")],
    names=["lvl0", "lvl1"],
)

df = DataFrame(
    np.arange(16, dtype="int64").reshape(4, 4), index=index, columns=columns
)
df = df.sort_index(axis=0).sort_index(axis=1)

# identity
result = df.loc[(slice(None), slice(None)), :]
tm.assert_frame_equal(result, df)
result = df.loc[(slice(None), slice(None)), (slice(None), slice(None))]
tm.assert_frame_equal(result, df)
result = df.loc[:, (slice(None), slice(None))]
tm.assert_frame_equal(result, df)

# index
result = df.loc[(slice(None), [1]), :]
expected = df.iloc[[0, 3]]
tm.assert_frame_equal(result, expected)

result = df.loc[(slice(None), 1), :]
expected = df.iloc[[0, 3]]
tm.assert_frame_equal(result, expected)

# columns
result = df.loc[:, (slice(None), ["foo"])]
expected = df.iloc[:, [1, 3]]
tm.assert_frame_equal(result, expected)

# both
result = df.loc[(slice(None), 1), (slice(None), ["foo"])]
expected = df.iloc[[0, 3], [1, 3]]
tm.assert_frame_equal(result, expected)

result = df.loc["A", "a"]
expected = DataFrame(
    {"bar": [1, 5, 9], "foo": [0, 4, 8]},
    index=Index([1, 2, 3], name="two"),
    columns=Index(["bar", "foo"], name="lvl1"),
)
tm.assert_frame_equal(result, expected)

result = df.loc[(slice(None), [1, 2]), :]
expected = df.iloc[[0, 1, 3]]
tm.assert_frame_equal(result, expected)

# multi-level series
s = Series(np.arange(len(ix.to_numpy())), index=ix)
result = s.loc["A1":"A3", :, ["C1", "C3"]]
expected = s.loc[
    [
        (
            a,
            b,
            c,
            d,
        )
        for a, b, c, d in s.index.values
        if a in ("A1", "A2", "A3") and c in ("C1", "C3")
    ]
]
tm.assert_series_equal(result, expected)

# boolean indexers
result = df.loc[(slice(None), df.loc[:, ("a", "bar")] > 5), :]
expected = df.iloc[[2, 3]]
tm.assert_frame_equal(result, expected)

msg = (
    "cannot index with a boolean indexer "
    "that is not the same length as the index"
)
with pytest.raises(ValueError, match=msg):
    df.loc[(slice(None), np.array([True, False])), :]

with pytest.raises(KeyError, match=r"\[1\] not in index"):
    # slice(None) is on the index, [1] is on the columns, but 1 is
    #  not in the columns, so we raise
    #  This used to treat [1] as positional GH#16396
    df.loc[slice(None), [1]]

# not lexsorted
assert df.index._lexsort_depth == 2
df = df.sort_index(level=1, axis=0)
assert df.index._lexsort_depth == 0

msg = (
    "MultiIndex slicing requires the index to be "
    r"lexsorted: slicing on levels \[1\], lexsort depth 0"
)
with pytest.raises(UnsortedIndexError, match=msg):
    df.loc[(slice(None), slice("bar")), :]

# GH 16734: not sorted, but no real slicing
result = df.loc[(slice(None), df.loc[:, ("a", "bar")] > 5), :]
tm.assert_frame_equal(result, df.iloc[[1, 3], :])
