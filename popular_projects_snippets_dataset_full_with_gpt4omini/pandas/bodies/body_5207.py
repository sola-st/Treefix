# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
res = td.to_pytimedelta()
expected = timedelta(days=106752)
assert type(res) is timedelta
assert res == expected
