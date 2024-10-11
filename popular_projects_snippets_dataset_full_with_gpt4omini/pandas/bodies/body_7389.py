# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_sorting.py
# https://pandas.pydata.org/pandas-docs/stable/advanced.html#sorting-a-multiindex
dfm = DataFrame(
    {"jim": [0, 0, 1, 1], "joe": ["x", "x", "z", "y"], "jolie": np.random.rand(4)}
)

dfm = dfm.set_index(["jim", "joe"])
with tm.assert_produces_warning(PerformanceWarning):
    dfm.loc[(1, "z")]

msg = r"Key length \(2\) was greater than MultiIndex lexsort depth \(1\)"
with pytest.raises(UnsortedIndexError, match=msg):
    dfm.loc[(0, "y"):(1, "z")]

assert not dfm.index._is_lexsorted()
assert dfm.index._lexsort_depth == 1

# sort it
dfm = dfm.sort_index()
dfm.loc[(1, "z")]
dfm.loc[(0, "y"):(1, "z")]

assert dfm.index._is_lexsorted()
assert dfm.index._lexsort_depth == 2
