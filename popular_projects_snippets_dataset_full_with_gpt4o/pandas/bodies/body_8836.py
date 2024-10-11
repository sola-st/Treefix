# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
res = next(iter(dta))
expected = dta[0]

assert type(res) is pd.Timestamp
assert res.value == expected.value
assert res._creso == expected._creso
assert res == expected
