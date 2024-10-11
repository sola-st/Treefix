# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH: 19556
mi = MultiIndex.from_arrays(
    [
        np.array(["a", "a", "b", "b"]),
        np.array(["1", "2", "2", "3"]),
        np.array(["c", "d", "c", "d"]),
    ],
    names=["one", "two", "three"],
)
df = DataFrame(np.random.rand(4, 3), index=mi)
msg = r"\('b', '1', slice\(None, None, None\)\)"
with pytest.raises(KeyError, match=msg):
    df.loc[("b", "1", slice(None)), :]
with pytest.raises(KeyError, match=msg):
    df.index.get_locs(("b", "1", slice(None)))
with pytest.raises(KeyError, match=r"\('b', '1'\)"):
    df.loc[("b", "1"), :]
