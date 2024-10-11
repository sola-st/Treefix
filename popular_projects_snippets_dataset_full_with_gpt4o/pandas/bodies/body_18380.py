# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
expected = Series(["29.5D", "29.5D", "NaT"], dtype="timedelta64[ns]")

tdser = tm.box_expected(tdser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = tdser // two
tm.assert_equal(result, expected)

with pytest.raises(TypeError, match="Cannot divide"):
    two // tdser
