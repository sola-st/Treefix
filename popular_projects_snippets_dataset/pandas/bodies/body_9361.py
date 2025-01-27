# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
"""Fixture yielding 'registry' with no DecimalDtype entries"""
idx = registry.dtypes.index(DecimalDtype)
registry.dtypes.pop(idx)
exit()
registry.dtypes.append(DecimalDtype)
