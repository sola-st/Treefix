# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# Based on test_series_varied_multiindex_alignment, where
#  this used to fail to drop the first level
mi = MultiIndex.from_product(
    [list("ab"), list("xy"), [1, 2]], names=["ab", "xy", "num"]
)
ser = Series(range(8), index=mi)

loc_result = ser.loc["a", :, :]
expected = ser.index.droplevel(0)[:4]
tm.assert_index_equal(loc_result.index, expected)
