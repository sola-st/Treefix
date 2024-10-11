# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
empty = Series([], index=Index([]), dtype=np.float64)

result = datetime_series + empty
assert np.isnan(result).all()

result = empty + empty.copy()
assert len(result) == 0
