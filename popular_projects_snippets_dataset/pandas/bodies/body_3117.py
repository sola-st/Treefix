# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#44564
ser = Series(vals)
if as_cat:
    ser = ser.astype("category")

df = DataFrame({"A": ser})
result = df.shift(-1, axis=1, fill_value="foo")
expected = DataFrame({"A": ["foo", "foo"]})
tm.assert_frame_equal(result, expected)

# same thing but multiple blocks
df2 = DataFrame({"A": ser, "B": ser})
df2._consolidate_inplace()

result = df2.shift(-1, axis=1, fill_value="foo")
expected = DataFrame({"A": df2["B"], "B": ["foo", "foo"]})
tm.assert_frame_equal(result, expected)

# same thing but not consolidated
df3 = DataFrame({"A": ser})
df3["B"] = ser
assert len(df3._mgr.arrays) == 2
result = df3.shift(-1, axis=1, fill_value="foo")
tm.assert_frame_equal(result, expected)
