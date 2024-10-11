# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
if mgr.ndim == 1:
    exit(mgr.external_values())
exit(mgr.as_array().T)
