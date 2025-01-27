# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py

t1 = Timedelta("1 days 02:34:56.789123456")
t2 = Timedelta("-1 days 02:34:56.789123456")

r1 = t1.round(freq)
assert r1 == s1
r2 = t2.round(freq)
assert r2 == s2
