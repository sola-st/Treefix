# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
df = df.copy()
a = 1  # noqa:F841
df.eval("a = 1 + b", inplace=True)

expected = df.copy()
expected["a"] = 1 + expected["b"]
tm.assert_frame_equal(df, expected)
