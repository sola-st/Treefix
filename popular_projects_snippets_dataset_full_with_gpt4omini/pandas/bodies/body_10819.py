# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 13420
df = DataFrame({"a": [1, 2, 3, 4], "b": [-1, -2, -3, -4], "c": [5, 6, 7, 8]})
cat = Categorical.from_codes(code, categories=list("abc"))
result = df.groupby(cat, axis=1).mean()
expected = df.T.groupby(cat, axis=0).mean().T
tm.assert_frame_equal(result, expected)
