# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
result = data_missing[0]
assert na_cmp(result, na_value)
