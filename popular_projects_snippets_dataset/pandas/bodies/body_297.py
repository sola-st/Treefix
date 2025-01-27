# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = tm.makeCustomDataframe(
    10, 10, data_gen_f=f, r_idx_type=r_idx_type, c_idx_type=c_idx_type
)
res = pd.eval("df < 2", engine=engine, parser=parser)
tm.assert_frame_equal(res, df < 2)

df3 = DataFrame(np.random.randn(*df.shape), index=df.index, columns=df.columns)
res = pd.eval("df < df3", engine=engine, parser=parser)
tm.assert_frame_equal(res, df < df3)
