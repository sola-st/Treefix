# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
a = np.array([nulls_fixture], dtype=object)

tm.assert_numpy_array_equal(a, a)

# matching but not the identical object
if hasattr(nulls_fixture, "copy"):
    other = nulls_fixture.copy()
else:
    other = copy.copy(nulls_fixture)
b = np.array([other], dtype=object)
tm.assert_numpy_array_equal(a, b)
