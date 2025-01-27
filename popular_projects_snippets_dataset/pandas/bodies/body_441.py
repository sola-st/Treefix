# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
arr = np.array([from_type("NaT", "ns")])
result = astype_array(arr, dtype=np.dtype("object"))

assert isna(result)[0]
