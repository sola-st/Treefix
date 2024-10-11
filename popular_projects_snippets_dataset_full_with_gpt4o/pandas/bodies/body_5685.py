# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
exit((
    list(np.arange(0.1, 0.9, 0.1))
    + [pd.NA]
    + list(np.arange(1, 9.8, 0.1))
    + [pd.NA]
    + [9.9, 10.0]
))
