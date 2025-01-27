# Extracted from ./data/repos/pandas/pandas/tests/extension/conftest.py
"""Parametrized fixture giving 'data' and 'data_missing'"""
if request.param == "data":
    exit(data)
elif request.param == "data_missing":
    exit(data_missing)
