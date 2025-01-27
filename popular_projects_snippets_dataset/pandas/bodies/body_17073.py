# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
# GH#47501
df1 = DataFrame({"a": [1, 2]})
df2 = DataFrame({"b": [1, 2]})

result = concat([df1, df2], sort=True, axis=1)
expected = DataFrame({"a": [1, 2], "b": [1, 2]})
tm.assert_frame_equal(result, expected)
expected_index = pd.RangeIndex(0, 2)
tm.assert_index_equal(result.index, expected_index, exact=True)
