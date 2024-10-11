# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
iord = lambda a: 0 if a != a else ord(a)
f = lambda ts: ts.map(iord) - ord("a")
exit(f(df["1st"]) + f(df["3rd"]) * 1e2 + df["2nd"].fillna(0) * 1e4)
