# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always", RuntimeWarning)

    df = tm.makeCustomDataframe(
        3, 2, data_gen_f=f, r_idx_type=r1, c_idx_type=c1
    )
    df2 = tm.makeCustomDataframe(
        4, 2, data_gen_f=f, r_idx_type=r2, c_idx_type=c2
    )
    df3 = tm.makeCustomDataframe(
        5, 2, data_gen_f=f, r_idx_type=r2, c_idx_type=c2
    )
    if should_warn(df.index, df2.index, df3.index):
        with tm.assert_produces_warning(RuntimeWarning):
            res = pd.eval("df + df2 + df3", engine=engine, parser=parser)
    else:
        res = pd.eval("df + df2 + df3", engine=engine, parser=parser)
    tm.assert_frame_equal(res, df + df2 + df3)
