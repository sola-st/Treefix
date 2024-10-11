# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
# explicit targets
self.eval("c = df.a + df.b", local_dict={"df": df}, target=df, inplace=True)
expected = df.copy()
expected["c"] = expected["a"] + expected["b"]
tm.assert_frame_equal(df, expected)
