# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# GH 17091
df = DataFrame({"data": range(6), "key": list("ABCABC")})
grouper = df.groupby("key")
result = grouper.filter(lambda x: True)
expected = DataFrame({"data": range(6), "key": list("ABCABC")})
tm.assert_frame_equal(result, expected)

grouper.sum()
result = grouper.filter(lambda x: True)
tm.assert_frame_equal(result, expected)
