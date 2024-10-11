# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH#35382
df = DataFrame({"a": [1, 0, 1]})

result = df.merge(df, on="a", how=how, sort=sort)
expected = DataFrame(values, columns=["a"])
tm.assert_frame_equal(result, expected)
