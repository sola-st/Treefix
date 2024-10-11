# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
# PandasArray[object] can hold anything, so skip
super().test_insert_invalid(data, invalid_scalar)
