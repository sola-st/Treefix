# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
# GH#17213, GH#13918
cols = ["a", "b", "c"]
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=cols)
for c, (k, v) in zip(cols, df.items()):
    assert c == k
    assert isinstance(v, Series)
    assert (df[k] == v).all()
