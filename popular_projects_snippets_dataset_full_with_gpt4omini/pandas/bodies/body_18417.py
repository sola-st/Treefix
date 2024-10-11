# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#11034
box = box_with_array

ser = Series([Timestamp("2000-01-29 01:59:00"), Timestamp("2000-01-30"), NaT])
ser = tm.box_expected(ser, box)
xbox = get_upcast_box(ser, ser, True)

result = ser != ser
expected = tm.box_expected([False, False, True], xbox)
tm.assert_equal(result, expected)

if box is pd.DataFrame:
    # alignment for frame vs series comparisons deprecated
    #  in GH#46795 enforced 2.0
    with pytest.raises(ValueError, match="not aligned"):
        ser != ser[0]

else:
    result = ser != ser[0]
    expected = tm.box_expected([False, True, True], xbox)
    tm.assert_equal(result, expected)

if box is pd.DataFrame:
    # alignment for frame vs series comparisons deprecated
    #  in GH#46795 enforced 2.0
    with pytest.raises(ValueError, match="not aligned"):
        ser != ser[2]
else:
    result = ser != ser[2]
    expected = tm.box_expected([True, True, True], xbox)
    tm.assert_equal(result, expected)

result = ser == ser
expected = tm.box_expected([True, True, False], xbox)
tm.assert_equal(result, expected)

if box is pd.DataFrame:
    # alignment for frame vs series comparisons deprecated
    #  in GH#46795 enforced 2.0
    with pytest.raises(ValueError, match="not aligned"):
        ser == ser[0]
else:
    result = ser == ser[0]
    expected = tm.box_expected([True, False, False], xbox)
    tm.assert_equal(result, expected)

if box is pd.DataFrame:
    # alignment for frame vs series comparisons deprecated
    #  in GH#46795 enforced 2.0
    with pytest.raises(ValueError, match="not aligned"):
        ser == ser[2]
else:
    result = ser == ser[2]
    expected = tm.box_expected([False, False, False], xbox)
    tm.assert_equal(result, expected)
