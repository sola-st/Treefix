# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 16363
df = DataFrame({"x": np.array([0], dtype=dtype)})
res = df.eval(expr)
assert res.values == np.array([False])
