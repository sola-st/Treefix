# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#26049

df = DataFrame([1, 2, 3, 4], columns=["col1"], dtype="uint8")
df.loc[2, "col1"] = value  # value that can't be held in uint8

expected = DataFrame([1, 2, 300, 4], columns=["col1"], dtype="uint16")
tm.assert_frame_equal(df, expected)
