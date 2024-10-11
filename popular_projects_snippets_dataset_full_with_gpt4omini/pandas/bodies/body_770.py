# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array([1, 2])
msg = "elementwise comparison failed"
cm = (
    # stacklevel is chosen to make sense when called from .equals
    tm.assert_produces_warning(FutureWarning, match=msg, check_stacklevel=False)
    if isinstance(val, str) and not is_numpy_dev
    else nullcontext()
)
with cm:
    assert not array_equivalent(Series([arr, arr]), Series([arr, val]))
