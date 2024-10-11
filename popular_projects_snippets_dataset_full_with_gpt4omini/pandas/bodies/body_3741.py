# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH 25087
ii = pd.IntervalIndex.from_breaks([0, 2.78, 3.14, 6.28])
ci = pd.CategoricalIndex(ii)
df = DataFrame({"A": list("abc")}, index=ci)

expected = df
result = df.dropna()
tm.assert_frame_equal(result, expected)
