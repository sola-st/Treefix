# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = tm.makeCustomDataframe(5, 3, data_gen_f=f, dtype=dt)
left, right = left_right
s = f"{left} {op} {right}"
res = pd.eval(s, engine=engine, parser=parser)
assert df.values.dtype == dt
assert res.values.dtype == dt
tm.assert_frame_equal(res, eval(s))
