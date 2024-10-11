# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))

a = 1  # noqa:F841
old_a = df.a.copy()
df.eval("a = a + b", inplace=True)
result = old_a + df.b
tm.assert_series_equal(result, df.a, check_names=False)
assert result.name is None
