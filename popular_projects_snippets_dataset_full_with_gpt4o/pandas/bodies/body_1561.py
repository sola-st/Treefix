# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#34318: test that you can access a None value using .loc
#  through a Multiindex

ser = Series([None], MultiIndex.from_arrays([["Level1"], ["Level2"]]))
result = ser.loc[("Level1", "Level2")]
assert result is None

midx = MultiIndex.from_product([["Level1"], ["Level2_a", "Level2_b"]])
ser = Series([None] * len(midx), dtype=object, index=midx)
result = ser.loc[("Level1", "Level2_a")]
assert result is None

ser = Series([1] * len(midx), dtype=object, index=midx)
result = ser.loc[("Level1", "Level2_a")]
assert result == 1
