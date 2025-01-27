# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
n = 3
m1 = 5
m2 = 2 * m1

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always", RuntimeWarning)

    index_name = random.choice(["index", "columns"])
    obj_name = random.choice(["df", "df2"])

    df = tm.makeCustomDataframe(
        m1, n, data_gen_f=f, r_idx_type=r1, c_idx_type=c1
    )
    df2 = tm.makeCustomDataframe(
        m2, n, data_gen_f=f, r_idx_type=r2, c_idx_type=c2
    )
    index = getattr(locals().get(obj_name), index_name)
    ser = Series(np.random.randn(n), index[:n])

    if r2 == "dt" or c2 == "dt":
        if engine == "numexpr":
            expected2 = df2.add(ser)
        else:
            expected2 = df2 + ser
    else:
        expected2 = df2 + ser

    if r1 == "dt" or c1 == "dt":
        if engine == "numexpr":
            expected = expected2.add(df)
        else:
            expected = expected2 + df
    else:
        expected = expected2 + df

    if should_warn(df2.index, ser.index, df.index):
        with tm.assert_produces_warning(RuntimeWarning):
            res = pd.eval("df2 + ser + df", engine=engine, parser=parser)
    else:
        res = pd.eval("df2 + ser + df", engine=engine, parser=parser)
    assert res.shape == expected.shape
    tm.assert_frame_equal(res, expected)
