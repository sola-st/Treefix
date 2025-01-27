# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3), columns=list("abc"))
expr1 = "df.a < df.b"
expec1 = df.a < df.b
expr2 = "df.a + df.b + df.c"
expec2 = df.a + df.b + df.c
expr3 = "df.a + df.b + df.c[df.b < 0]"
expec3 = df.a + df.b + df.c[df.b < 0]
exprs = expr1, expr2, expr3
expecs = expec1, expec2, expec3
for e, expec in zip(exprs, expecs):
    tm.assert_series_equal(expec, self.eval(e, local_dict={"df": df}))
