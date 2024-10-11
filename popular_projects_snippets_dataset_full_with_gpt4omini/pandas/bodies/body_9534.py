# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
result = tda + pd.NaT
assert isinstance(result, TimedeltaArray)
assert result._creso == tda._creso
assert result.isna().all()

result = pd.NaT + tda
assert isinstance(result, TimedeltaArray)
assert result._creso == tda._creso
assert result.isna().all()
