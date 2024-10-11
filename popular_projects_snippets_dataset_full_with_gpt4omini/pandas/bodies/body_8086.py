# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py

if nulls_fixture is pd.NaT or nulls_fixture is pd.NA:
    # Check 1) that we cannot construct a float64 Index with this value
    #  and 2) that with an NaN we do not have .isin(nulls_fixture)
    msg = "data is not compatible with NumericIndex"
    with pytest.raises(ValueError, match=msg):
        NumericIndex([1.0, nulls_fixture], dtype=np.float64)

    idx = NumericIndex([1.0, np.nan], dtype=np.float64)
    assert not idx.isin([nulls_fixture]).any()
    exit()

idx = NumericIndex([1.0, nulls_fixture], dtype=np.float64)
res = idx.isin([np.nan])
tm.assert_numpy_array_equal(res, np.array([False, True]))

# we cannot compare NaT with NaN
res = idx.isin([pd.NaT])
tm.assert_numpy_array_equal(res, np.array([False, False]))
