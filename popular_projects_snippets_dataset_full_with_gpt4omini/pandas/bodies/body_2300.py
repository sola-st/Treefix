# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# where inplace

def _check_set(df, cond, check_dtypes=True):
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

df = where_frame
if df is float_string_frame:
    msg = "'>' not supported between instances of 'str' and 'int'"
    with pytest.raises(TypeError, match=msg):
        df > 0
    exit()

cond = df > 0
_check_set(df, cond)

cond = df >= 0
_check_set(df, cond)

# aligning
cond = (df >= 0)[1:]
_check_set(df, cond)
