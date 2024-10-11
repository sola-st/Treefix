# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
arr = SparseArray(data, dtype=dtype)
result = getattr(arr, func)()
if expected is NaT:
    # TODO: pin down whether we wrap datetime64("NaT")
    assert result is NaT or np.isnat(result)
else:
    assert np.isnan(result)
