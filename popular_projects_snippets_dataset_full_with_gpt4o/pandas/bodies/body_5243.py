# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH 11129
v = Timedelta(1, "D")
td = timedelta(days=1)
assert hash(v) == hash(td)

d = {td: 2}
assert d[v] == 2

tds = [Timedelta(seconds=1) + Timedelta(days=n) for n in range(20)]
assert all(hash(td) == hash(td.to_pytimedelta()) for td in tds)

# python timedeltas drop ns resolution
ns_td = Timedelta(1, "ns")
assert hash(ns_td) != hash(ns_td.to_pytimedelta())
