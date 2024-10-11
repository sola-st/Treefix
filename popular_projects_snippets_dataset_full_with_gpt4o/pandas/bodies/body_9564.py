# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/conftest.py
"""Parametrized fixture returning 'data' or 'data_missing' float arrays.

    Used to test dtype conversion with and without missing values.
    """
if request.param == "data":
    exit(data)
elif request.param == "data_missing":
    exit(data_missing)
