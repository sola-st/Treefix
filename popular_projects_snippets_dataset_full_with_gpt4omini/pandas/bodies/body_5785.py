# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# https://github.com/pandas-dev/pandas/issues/34660
assert pd.Series(data).equals(pd.Series(data))
