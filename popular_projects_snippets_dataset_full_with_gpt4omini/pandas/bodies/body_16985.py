# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH 15328
df_empty = DataFrame()
df_a = DataFrame({"a": [1, 2]}, index=[0, 1], dtype="int64")
df_expected = DataFrame({"a": []}, index=RangeIndex(0), dtype="int64")

for how, expected in [("inner", df_expected), ("outer", df_a)]:
    result = concat([df_a, df_empty], axis=1, join=how)
    tm.assert_frame_equal(result, expected)
