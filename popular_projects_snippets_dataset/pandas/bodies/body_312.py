# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3))
result = self.eval("(df + 1)[df > 2]", local_dict={"df": df})
expected = (df + 1)[df > 2]
tm.assert_frame_equal(result, expected)
