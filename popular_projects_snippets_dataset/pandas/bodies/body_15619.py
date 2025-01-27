# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_equals.py
# GH20676 Verify equals operator for list of Numpy arrays
arr = np.array([1, 2])
s1 = Series([arr, arr])
s2 = s1.copy()
assert s1.equals(s2)

s1[1] = val

cm = (
    tm.assert_produces_warning(FutureWarning, check_stacklevel=False)
    if isinstance(val, str) and not is_numpy_dev
    else nullcontext()
)
with cm:
    assert not s1.equals(s2)
