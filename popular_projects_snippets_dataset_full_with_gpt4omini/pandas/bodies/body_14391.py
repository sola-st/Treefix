# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
with catch_warnings(record=True):
    values = np.random.randn(2)

    func = lambda lhs, rhs: tm.assert_series_equal(lhs, rhs, check_index_type=True)

with catch_warnings(record=True):
    ser = Series(values, [0, "y"])
    _check_roundtrip(ser, func, path=setup_path)

with catch_warnings(record=True):
    ser = Series(values, [datetime.datetime.today(), 0])
    _check_roundtrip(ser, func, path=setup_path)

with catch_warnings(record=True):
    ser = Series(values, ["y", 0])
    _check_roundtrip(ser, func, path=setup_path)

with catch_warnings(record=True):
    ser = Series(values, [datetime.date.today(), "a"])
    _check_roundtrip(ser, func, path=setup_path)

with catch_warnings(record=True):
    ser = Series(values, [0, "y"])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, [datetime.datetime.today(), 0])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, ["y", 0])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, [datetime.date.today(), "a"])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, [1.23, "b"])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, [1, 1.53])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(values, [1, 5])
    _check_roundtrip(ser, func, path=setup_path)

    ser = Series(
        values, [datetime.datetime(2012, 1, 1), datetime.datetime(2012, 1, 2)]
    )
    _check_roundtrip(ser, func, path=setup_path)
