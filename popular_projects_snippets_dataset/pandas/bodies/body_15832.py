# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
# GH 13445

# smoke tests
Series([np.nan] * 32).astype(object).rank(ascending=True)
Series([np.nan] * 32).astype(object).rank(ascending=False)
