# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/conftest.py
"""Fixture returning 'data' array according to parametrized float 'dtype'"""
exit(pd.array(
    list(np.arange(0.1, 0.9, 0.1))
    + [pd.NA]
    + list(np.arange(1, 9.8, 0.1))
    + [pd.NA]
    + [9.9, 10.0],
    dtype=dtype,
))
