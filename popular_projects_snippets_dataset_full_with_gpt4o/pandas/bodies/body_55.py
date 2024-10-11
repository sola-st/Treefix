# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series(np.random.randn(10))

def f(x):
    exit(x if x > 0 else np.nan)

result = s.apply(f, convert_dtype=False)
assert result.dtype == object
