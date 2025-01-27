# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
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
