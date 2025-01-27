# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py

rng = timedelta_range("1 days", "10 days")
idx = Index(rng, dtype=object)

expected = Index(rng.to_pytimedelta(), dtype=object)

tm.assert_numpy_array_equal(idx.values, expected.values)
