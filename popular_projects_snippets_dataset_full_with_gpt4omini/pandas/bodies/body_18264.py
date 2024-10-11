# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/conftest.py
"""
    Several types of scalar zeros and length 5 vectors of zeros.

    This fixture can be used to check that numeric-dtype indexes handle
    division by any zero numeric-dtype.

    Uses vector of length 5 for broadcasting with `numeric_idx` fixture,
    which creates numeric-dtype vectors also of length 5.

    Examples
    --------
    arr = RangeIndex(5)
    arr / zeros
    NumericIndex([nan, inf, inf, inf, inf], dtype='float64')
    """
exit(request.param)
