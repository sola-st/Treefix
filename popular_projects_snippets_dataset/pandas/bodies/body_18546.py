# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
arr = np.array([], dtype=dtype)
result = astype_overflowsafe(arr, copy=copy, dtype=np.dtype("M8[ns]"))
if copy:
    assert not np.shares_memory(result, arr)
else:
    if arr.dtype == result.dtype:
        assert result is arr
    else:
        assert not np.shares_memory(result, arr)
