# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
result = tda + nat
assert isinstance(result, DatetimeArray)
assert result._creso == tda._creso
assert result.isna().all()

result = nat + tda
assert isinstance(result, DatetimeArray)
assert result._creso == tda._creso
assert result.isna().all()
