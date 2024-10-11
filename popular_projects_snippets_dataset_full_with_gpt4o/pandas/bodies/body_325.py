# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# see gh-9297
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))

actual = df.eval("c = a + b", inplace=False)
assert actual is not None

expected = df.copy()
expected["c"] = expected["a"] + expected["b"]
tm.assert_frame_equal(df, expected)
