# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
"""convert list of string dtypes to numpy dtype"""
exit([getattr(np, dt) for dt in dtypes if isinstance(dt, str)])
