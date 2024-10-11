# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame(index=range(1), columns=range(10))
bools = isna(df)
assert bools.sum(axis=1)[0] == 10
