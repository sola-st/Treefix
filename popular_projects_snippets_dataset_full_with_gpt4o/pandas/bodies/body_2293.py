# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
other1 = _safe_add(df)
rs = df.where(cond, other1)
rs2 = df.where(cond.values, other1)
for k, v in rs.items():
    exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index)
    tm.assert_series_equal(v, exp, check_names=False)
tm.assert_frame_equal(rs, rs2)

# dtypes
if check_dtypes:
    assert (rs.dtypes == df.dtypes).all()
