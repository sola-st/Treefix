# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
arr = np.array([invalid_date], dtype="object")
kwargs = {"values": arr, "errors": errors}

if errors == "raise":
    msg = "^Out of bounds nanosecond timestamp: .*, at position 0$"

    with pytest.raises(ValueError, match=msg):
        tslib.array_to_datetime(**kwargs)
else:  # coerce.
    result, _ = tslib.array_to_datetime(**kwargs)
    expected = np.array([iNaT], dtype="M8[ns]")

    tm.assert_numpy_array_equal(result, expected)
