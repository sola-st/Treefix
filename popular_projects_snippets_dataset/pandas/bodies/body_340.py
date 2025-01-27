# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = tm.makeCustomDataframe(2, 2, data_gen_f=f, c_idx_type="p", r_idx_type="i")
r = self.eval("df[df[df < 2] < 2] + df * 2", local_dict={"df": df})
e = df[df[df < 2] < 2] + df * 2
tm.assert_frame_equal(r, e)
