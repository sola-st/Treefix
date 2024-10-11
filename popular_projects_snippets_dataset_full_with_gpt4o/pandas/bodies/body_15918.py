# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
# covers #9694
assert pd.isna(Series([], dtype="M8[ns]").quantile(0.5))
assert pd.isna(Series([], dtype="m8[ns]").quantile(0.5))
