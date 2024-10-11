# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert not isna_f(1.0)
assert isna_f(None)
assert isna_f(np.NaN)
assert float("nan")
assert not isna_f(np.inf)
assert not isna_f(-np.inf)

# type
assert not isna_f(type(Series(dtype=object)))
assert not isna_f(type(Series(dtype=np.float64)))
assert not isna_f(type(pd.DataFrame()))
