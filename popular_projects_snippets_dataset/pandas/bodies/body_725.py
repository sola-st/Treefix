# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
idx = pd.IntervalIndex.from_breaks(range(5), closed="both")
if asobject:
    idx = idx.astype(object)

inferred = lib.infer_dtype(idx, skipna=False)
assert inferred == "interval"

inferred = lib.infer_dtype(idx._data, skipna=False)
assert inferred == "interval"

inferred = lib.infer_dtype(Series(idx, dtype=idx.dtype), skipna=False)
assert inferred == "interval"
