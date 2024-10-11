# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# Test cartesian product of null fixtures and ensure that we don't
# mangle the various types (save a corner case with PyPy)

# all nans are the same
if (
    isinstance(nulls_fixture, float)
    and isinstance(nulls_fixture2, float)
    and math.isnan(nulls_fixture)
    and math.isnan(nulls_fixture2)
):
    tm.assert_numpy_array_equal(
        Index(["a", nulls_fixture]).isin([nulls_fixture2]),
        np.array([False, True]),
    )

elif nulls_fixture is nulls_fixture2:  # should preserve NA type
    tm.assert_numpy_array_equal(
        Index(["a", nulls_fixture]).isin([nulls_fixture2]),
        np.array([False, True]),
    )

else:
    tm.assert_numpy_array_equal(
        Index(["a", nulls_fixture]).isin([nulls_fixture2]),
        np.array([False, False]),
    )
