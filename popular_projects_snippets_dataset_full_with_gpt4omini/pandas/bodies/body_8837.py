# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
result = dta.astype(object)
assert all(x._creso == dta._creso for x in result)
assert all(x == y for x, y in zip(result, dta))
