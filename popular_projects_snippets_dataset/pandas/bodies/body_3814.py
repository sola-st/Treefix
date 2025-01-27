# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH#1532
df1 = DataFrame({"a": [1, 1], "b": [1, 2], "x": [1, 2]})
df2 = DataFrame({"a": [2, 2], "b": [1, 2], "y": [1, 2]})
df1 = df1.set_index(["a", "b"])
df2 = df2.set_index(["a", "b"])
# it works!
for how in ["left", "right", "outer"]:
    df1.join(df2, how=how)
