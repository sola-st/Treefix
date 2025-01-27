# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame({"a": np.random.randn(10)})
a = df.a

expr = f"{fn}(a)"
got = self.eval(expr)
with np.errstate(all="ignore"):
    expect = getattr(np, fn)(a)
tm.assert_series_equal(got, expect, check_names=False)
