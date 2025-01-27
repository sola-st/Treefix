# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always", RuntimeWarning)
    df = tm.makeCustomDataframe(
        10, 10, data_gen_f=f, r_idx_type=r_idx_type, c_idx_type=c_idx_type
    )
    index = getattr(df, index_name)
    s = Series(np.random.randn(5), index[:5])

    if should_warn(df.index, s.index):
        with tm.assert_produces_warning(RuntimeWarning):
            res = pd.eval("df + s", engine=engine, parser=parser)
    else:
        res = pd.eval("df + s", engine=engine, parser=parser)

    if r_idx_type == "dt" or c_idx_type == "dt":
        expected = df.add(s) if engine == "numexpr" else df + s
    else:
        expected = df + s
    tm.assert_frame_equal(res, expected)
