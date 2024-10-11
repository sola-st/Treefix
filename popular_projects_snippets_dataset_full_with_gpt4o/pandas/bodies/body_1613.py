# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# passing a list can include valid categories _or_ NA values
ci = CategoricalIndex(["A", "B", np.nan])
ser = Series(range(3), index=ci)

result = ser.loc[box(ci)]
tm.assert_series_equal(result, ser)

result = ser[box(ci)]
tm.assert_series_equal(result, ser)

result = ser.to_frame().loc[box(ci)]
tm.assert_frame_equal(result, ser.to_frame())

ser2 = ser[:-1]
ci2 = ci[1:]
# but if there are no NAs present, this should raise KeyError
msg = "not in index"
with pytest.raises(KeyError, match=msg):
    ser2.loc[box(ci2)]

with pytest.raises(KeyError, match=msg):
    ser2[box(ci2)]

with pytest.raises(KeyError, match=msg):
    ser2.to_frame().loc[box(ci2)]
