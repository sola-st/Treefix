# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 2786
df = DataFrame(np.random.random((3, 4)))
df2 = df.copy()
cols = ["a", "a", "a", "a"]
df.columns = cols

expected = df2.applymap(str)
expected.columns = cols
result = df.applymap(str)
tm.assert_frame_equal(result, expected)
