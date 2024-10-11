# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# aligning
def _check_align(df, cond, other, check_dtypes=True):
    rs = df.where(cond, other)
    for i, k in enumerate(rs.columns):
        result = rs[k]
        d = df[k].values
        c = cond[k].reindex(df[k].index).fillna(False).values

        if is_scalar(other):
            o = other
        else:
            if isinstance(other, np.ndarray):
                o = Series(other[:, i], index=result.index).values
            else:
                o = other[k].values

        new_values = d if c.all() else np.where(c, d, o)
        expected = Series(new_values, index=result.index, name=k)

        # since we can't always have the correct numpy dtype
        # as numpy doesn't know how to downcast, don't check
        tm.assert_series_equal(result, expected, check_dtype=False)

    # dtypes
    # can't check dtype when other is an ndarray

    if check_dtypes and not isinstance(other, np.ndarray):
        assert (rs.dtypes == df.dtypes).all()

df = where_frame
if df is float_string_frame:
    msg = "'>' not supported between instances of 'str' and 'int'"
    with pytest.raises(TypeError, match=msg):
        df > 0
    exit()

# other is a frame
cond = (df > 0)[1:]
_check_align(df, cond, _safe_add(df))

# check other is ndarray
cond = df > 0
_check_align(df, cond, (_safe_add(df).values))

# integers are upcast, so don't check the dtypes
cond = df > 0
check_dtypes = all(not issubclass(s.type, np.integer) for s in df.dtypes)
_check_align(df, cond, np.nan, check_dtypes=check_dtypes)
