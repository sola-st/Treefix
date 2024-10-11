# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
# single assignment - existing variable
expected = df.copy()
expected["a"] = expected["a"] + expected["b"]
df.eval("a = a + b", inplace=True)
tm.assert_frame_equal(df, expected)
