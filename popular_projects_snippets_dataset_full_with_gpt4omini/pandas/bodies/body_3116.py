# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#31971
ser = Series([pd.Timestamp("2020-01-01"), pd.Timestamp("2020-01-02")])

with pytest.raises(TypeError, match="value should be a"):
    ser.shift(1, fill_value=0)

df = ser.to_frame()
with pytest.raises(TypeError, match="value should be a"):
    df.shift(1, fill_value=0)

# axis = 1
df2 = DataFrame({"A": ser, "B": ser})
df2._consolidate_inplace()

result = df2.shift(1, axis=1, fill_value=0)
expected = DataFrame({"A": [0, 0], "B": df2["A"]})
tm.assert_frame_equal(result, expected)

# same thing but not consolidated; pre-2.0 we got different behavior
df3 = DataFrame({"A": ser})
df3["B"] = ser
assert len(df3._mgr.arrays) == 2
result = df3.shift(1, axis=1, fill_value=0)
tm.assert_frame_equal(result, expected)
