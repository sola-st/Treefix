# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#12089
ser = Series(
    date_range("2011-01-01", periods=3, tz="US/Eastern"),
    index=["a", "b", "c"],
)
s2 = ser.copy()
expected = Timestamp("2011-01-03", tz="US/Eastern")
s2.loc["a"] = expected
result = s2.loc["a"]
assert result == expected

s2 = ser.copy()
s2.iloc[0] = expected
result = s2.iloc[0]
assert result == expected

s2 = ser.copy()
s2["a"] = expected
result = s2["a"]
assert result == expected
