# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/conftest.py
"""
    Fixture returning array with missing data according to parametrized float
    'dtype'.
    """
exit(pd.array([np.nan, 0.1], dtype=dtype))
