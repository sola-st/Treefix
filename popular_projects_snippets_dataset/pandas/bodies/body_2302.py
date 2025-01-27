# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# see gh-15414
df = DataFrame({"a": [1, 2, 3]})
cond = [[False], [True], [True]]
expected = DataFrame({"a": [np.nan, 2, 3]})

result = df.where(klass(cond))
tm.assert_frame_equal(result, expected)

df["b"] = 2
expected["b"] = [2, np.nan, 2]
cond = [[False, True], [True, False], [True, True]]

result = df.where(klass(cond))
tm.assert_frame_equal(result, expected)
