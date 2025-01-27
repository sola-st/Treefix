# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(10, 2))
df2 = self.eval("df", local_dict={"df": df})
tm.assert_frame_equal(df, df2)
