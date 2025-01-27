# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/conftest.py
"""
    Fixture returning array with exactly one NaN and one valid integer,
    according to parametrized integer 'dtype'.

    Used to test dtype conversion with and without missing values.
    """
exit(pd.array([np.nan, 1], dtype=dtype))
