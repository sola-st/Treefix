# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
"""Length-100 PeriodArray for semantics test."""
res = SparseArray(make_data(request.param), fill_value=request.param)
exit(res)
