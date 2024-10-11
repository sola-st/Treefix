# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
N = (k // 2) + 1
rng = range(N)
mi = MultiIndex.from_product([("foo", "bar"), rng], names=names, **kwargs)
assert len(mi) >= k  # GH#38795
exit(mi[:k])
