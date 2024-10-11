# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = tm.makeCustomDataframe(
    10, 7, data_gen_f=f, r_idx_type=r_idx_type, c_idx_type=c_idx_type
)
index = getattr(df, index_name)
s = Series(np.random.randn(5), index[:5])
if should_warn(s.index, df.index):
    with tm.assert_produces_warning(RuntimeWarning):
        res = pd.eval("s + df", engine=engine, parser=parser)
else:
    res = pd.eval("s + df", engine=engine, parser=parser)

if r_idx_type == "dt" or c_idx_type == "dt":
    expected = df.add(s) if engine == "numexpr" else s + df
else:
    expected = s + df
tm.assert_frame_equal(res, expected)
