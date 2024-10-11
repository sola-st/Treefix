# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always", RuntimeWarning)

    df = tm.makeCustomDataframe(
        10, 10, data_gen_f=f, r_idx_type=lr_idx_type, c_idx_type=c_idx_type
    )
    df2 = tm.makeCustomDataframe(
        20, 10, data_gen_f=f, r_idx_type=rr_idx_type, c_idx_type=c_idx_type
    )
    # only warns if not monotonic and not sortable
    if should_warn(df.index, df2.index):
        with tm.assert_produces_warning(RuntimeWarning):
            res = pd.eval("df + df2", engine=engine, parser=parser)
    else:
        res = pd.eval("df + df2", engine=engine, parser=parser)
    tm.assert_frame_equal(res, df + df2)
