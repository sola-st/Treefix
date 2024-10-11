# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
s = "df * ~2"
df = tm.makeCustomDataframe(5, 3, data_gen_f=f)
res = pd.eval(s, engine=engine, parser=parser)
tm.assert_frame_equal(res, df * ~2)
