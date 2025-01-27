# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

# CSV with categoricals should result in the same output
# as when one would add a "normal" Series/DataFrame.
s = Series(pd.Categorical(["a", "b", "b", "a", "a", "c", "c", "c"]))
s2 = Series(["a", "b", "b", "a", "a", "c", "c", "c"])
res = StringIO()

s.to_csv(res, header=False)
exp = StringIO()

s2.to_csv(exp, header=False)
assert res.getvalue() == exp.getvalue()

df = DataFrame({"s": s})
df2 = DataFrame({"s": s2})

res = StringIO()
df.to_csv(res)

exp = StringIO()
df2.to_csv(exp)

assert res.getvalue() == exp.getvalue()
