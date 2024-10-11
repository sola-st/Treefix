# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#1590
df = DataFrame({"val": [0, 1, 2], "key": ["a", "b", "c"]})
expected = DataFrame({"val": [1, 2]}, Index(["b", "c"], name="key"))

df2 = df.loc[df.index.map(lambda indx: indx >= 1)]
result = df2.set_index("key")
tm.assert_frame_equal(result, expected)
