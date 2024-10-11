# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
dfi = df.copy()
econd = cond.reindex_like(df).fillna(True)
expected = dfi.mask(~econd)

return_value = dfi.where(cond, np.nan, inplace=True)
assert return_value is None
tm.assert_frame_equal(dfi, expected)

# dtypes (and confirm upcasts)x
if check_dtypes:
    for k, v in df.dtypes.items():
        if issubclass(v.type, np.integer) and not cond[k].all():
            v = np.dtype("float64")
        assert dfi[k].dtype == v
