# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/conftest.py
"""
    Fixture returning 'data' array with valid and missing values according to
    parametrized integer 'dtype'.

    Used to test dtype conversion with and without missing values.
    """
exit(pd.array(
    list(range(8)) + [np.nan] + list(range(10, 98)) + [np.nan] + [99, 100],
    dtype=dtype,
))
