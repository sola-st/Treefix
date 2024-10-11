# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_missing.py
# GH 6194
idx = MultiIndex.from_arrays(
    [
        [1, np.nan, 3, np.nan, 5],
        [1, 2, np.nan, np.nan, 5],
        ["a", "b", "c", np.nan, "e"],
    ]
)

exp = MultiIndex.from_arrays([[1, 5], [1, 5], ["a", "e"]])
tm.assert_index_equal(idx.dropna(), exp)
tm.assert_index_equal(idx.dropna(how="any"), exp)

exp = MultiIndex.from_arrays(
    [[1, np.nan, 3, 5], [1, 2, np.nan, 5], ["a", "b", "c", "e"]]
)
tm.assert_index_equal(idx.dropna(how="all"), exp)

msg = "invalid how option: xxx"
with pytest.raises(ValueError, match=msg):
    idx.dropna(how="xxx")

# GH26408
# test if missing values are dropped for multiindex constructed
# from codes and values
idx = MultiIndex(
    levels=[[np.nan, None, pd.NaT, "128", 2], [np.nan, None, pd.NaT, "128", 2]],
    codes=[[0, -1, 1, 2, 3, 4], [0, -1, 3, 3, 3, 4]],
)
expected = MultiIndex.from_arrays([["128", 2], ["128", 2]])
tm.assert_index_equal(idx.dropna(), expected)
tm.assert_index_equal(idx.dropna(how="any"), expected)

expected = MultiIndex.from_arrays(
    [[np.nan, np.nan, "128", 2], ["128", "128", "128", 2]]
)
tm.assert_index_equal(idx.dropna(how="all"), expected)
