# Extracted from ./data/repos/pandas/pandas/tests/test_aggregation.py
# GH 27519, test if make_unique function reorders correctly
result = _make_unique_kwarg_list(order)

assert result == expected_reorder
