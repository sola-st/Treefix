# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# setitem with boolean mask
mask = np.zeros(obj.shape, dtype=bool)
mask[key] = True

obj = obj.copy()

if is_list_like(val) and len(val) < mask.sum():
    msg = "boolean index did not match indexed array along dimension"
    with pytest.raises(IndexError, match=msg):
        indexer_sli(obj)[mask] = val
    exit()

indexer_sli(obj)[mask] = val
tm.assert_series_equal(obj, expected)
