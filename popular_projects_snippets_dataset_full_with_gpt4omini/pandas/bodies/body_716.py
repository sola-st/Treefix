# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py

dates = [date(2012, 1, day) for day in range(1, 20)]
index = Index(dates)
assert index.inferred_type == "date"

dates = [date(2012, 1, day) for day in range(1, 20)] + [np.nan]
result = lib.infer_dtype(dates, skipna=False)
assert result == "mixed"

result = lib.infer_dtype(dates, skipna=True)
assert result == "date"
