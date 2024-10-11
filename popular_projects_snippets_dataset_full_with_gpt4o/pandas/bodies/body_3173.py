# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# see gh-26303
index = Index([(1,), (2,), (3,)])
df = DataFrame([[1, 2, 3]], columns=index)
df = df.reindex(columns=[(1,), (3,)])
expected = ",1,3\n0,1,3\n"
result = df.to_csv(lineterminator="\n")
tm.assert_almost_equal(result, expected)
