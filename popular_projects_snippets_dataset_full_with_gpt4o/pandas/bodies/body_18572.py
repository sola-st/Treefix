# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
arr = np.array(["01-01-2013", "not_a_date", "1"], dtype=object)
kwargs = {"values": arr, "errors": errors}

if errors == "ignore":
    # Without coercing, the presence of any invalid
    # dates prevents any values from being converted.
    result, _ = tslib.array_to_datetime(**kwargs)
    tm.assert_numpy_array_equal(result, arr)
else:  # coerce.
    # With coercing, the invalid dates becomes iNaT
    result, _ = tslib.array_to_datetime(arr, errors="coerce")
    expected = ["2013-01-01T00:00:00.000000000", iNaT, iNaT]

    tm.assert_numpy_array_equal(result, np.array(expected, dtype="M8[ns]"))
