# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
op = comparison_op
tz = tz_aware_fixture
dti = date_range("2016-01-01", periods=2, tz=tz)

dtarr = tm.box_expected(dti, box_with_array)
xbox = get_upcast_box(dtarr, other, True)
if op in [operator.eq, operator.ne]:
    exbool = op is operator.ne
    expected = np.array([exbool, exbool], dtype=bool)
    expected = tm.box_expected(expected, xbox)

    result = op(dtarr, other)
    tm.assert_equal(result, expected)

    result = op(other, dtarr)
    tm.assert_equal(result, expected)
else:
    msg = (
        r"Invalid comparison between dtype=datetime64\[ns, .*\] "
        f"and {type(other).__name__}"
    )
    with pytest.raises(TypeError, match=msg):
        op(dtarr, other)
    with pytest.raises(TypeError, match=msg):
        op(other, dtarr)
