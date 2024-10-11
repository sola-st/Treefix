# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
"""Parametrized fixture returning 'data' or 'data_missing' integer arrays.

    Used to test dtype conversion with and without missing values.
    """
if request.param == "data":
    exit(data)
elif request.param == "data_missing":
    exit(data_missing)
