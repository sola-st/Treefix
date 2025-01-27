# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# GH#24282 check that Categorical.__cmp__(DataFrame) defers to frame
data = ["a", "b", 2, "a"]
cat = Categorical(data)

df = DataFrame(cat)

result = cat == df.T
expected = DataFrame([[True, True, True, True]])
tm.assert_frame_equal(result, expected)

result = cat[::-1] != df.T
expected = DataFrame([[False, True, True, False]])
tm.assert_frame_equal(result, expected)
