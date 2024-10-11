# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#42099
ser = Series([0, 1, 2, 3], dtype=dtype)
df = DataFrame({"data": ser})

result = DataFrame(index=df.index)
result.loc[df.index, "data"] = ser

tm.assert_frame_equal(result, df)

result = DataFrame(index=df.index)
result.loc[df.index, "data"] = ser._values
tm.assert_frame_equal(result, df)
