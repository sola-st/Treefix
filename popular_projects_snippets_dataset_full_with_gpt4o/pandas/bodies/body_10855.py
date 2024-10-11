# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
# GH 28662
data = np.array([1.0, np.nan, 1.0])
df = DataFrame({"key": data, "val": range(3)})

# Random segfaults; would have been guaranteed in loop
grp = df.groupby("key")
for _ in range(100):
    grp.quantile()
