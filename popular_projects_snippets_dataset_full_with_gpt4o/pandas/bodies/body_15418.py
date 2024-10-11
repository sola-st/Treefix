# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
mask = np.zeros(obj.shape, dtype=bool)
mask[key] = True

if is_list_like(val) and len(val) < len(obj):
    # Series.where is not valid here
    msg = "operands could not be broadcast together with shapes"
    with pytest.raises(ValueError, match=msg):
        obj.where(~mask, val)
    exit()

orig = obj
obj = obj.copy()
arr = obj._values

res = obj.where(~mask, val)
tm.assert_series_equal(res, expected)

self._check_inplace(is_inplace, orig, arr, obj)
