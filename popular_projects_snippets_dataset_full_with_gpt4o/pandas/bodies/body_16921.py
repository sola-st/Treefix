# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#47127
df1 = DataFrame({"A": [100], 0: 2})
result = concat([df1], ignore_index=True, join="inner", sort=True)
expected = DataFrame({0: [2], "A": [100]})
tm.assert_frame_equal(result, expected)
