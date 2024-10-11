# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH24386: Ensure dtypes are set correctly for an empty DataFrame.
# Empty DataFrame is generated via dictionary data with non-overlapping columns.
data = DataFrame({"a": [1, 2]}, columns=["b"], dtype=dtype)

if using_array_manager and dtype in tm.BYTES_DTYPES:
    # TODO(ArrayManager) astype to bytes dtypes does not yet give object dtype
    td.mark_array_manager_not_yet_implemented(request)

assert data.b.dtype.name == "object"
