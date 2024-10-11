# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#21168 KeyError, not "IndexingError: Too many indexers"
ser = Series(-1, index=MultiIndex.from_product([[0, 1]] * 2))

with pytest.raises(KeyError, match=r"\(0, 3\)"):
    ser.loc[0, 3]
