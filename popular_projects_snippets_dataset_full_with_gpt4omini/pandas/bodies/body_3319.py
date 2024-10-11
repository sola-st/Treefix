# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# GH 18271
df = DataFrame(
    {"A": np.arange(2**24 + 1), "B": np.arange(2**24 + 1, 0, -1)}
)
result = df.rank(pct=True).max()
assert (result == 1).all()
