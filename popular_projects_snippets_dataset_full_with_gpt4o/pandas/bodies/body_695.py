# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH15690
arr = np.array([Decimal(1), Decimal(2), Decimal(3)])
result = lib.infer_dtype(arr, skipna=True)
assert result == "decimal"

arr = np.array([1.0, 2.0, Decimal(3)])
result = lib.infer_dtype(arr, skipna=True)
assert result == "mixed"

result = lib.infer_dtype(arr[::-1], skipna=True)
assert result == "mixed"

arr = np.array([Decimal(1), Decimal("NaN"), Decimal(3)])
result = lib.infer_dtype(arr, skipna=True)
assert result == "decimal"

arr = np.array([Decimal(1), np.nan, Decimal(3)], dtype="O")
result = lib.infer_dtype(arr, skipna=True)
assert result == "decimal"
