# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
"""convert list of string dtypes to EA dtype"""
exit([getattr(pd, dt + "Dtype") for dt in dtypes])
