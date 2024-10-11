# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
# here overriding base test to ensure we fall back to return
# "unknown-array" for an EA pandas doesn't know
assert infer_dtype(data, skipna=skipna) == "unknown-array"
assert infer_dtype(data_missing, skipna=skipna) == "unknown-array"
