# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# GH#50162
per = pd.Period("2012-1-1", freq="D")
pi = pd.period_range("2012-1-1", periods=10, freq="D")
idx = per - pi

expected = pd.Index([x + per for x in idx], dtype=object)
result = idx + per
tm.assert_index_equal(result, expected)

result = per + idx
tm.assert_index_equal(result, expected)
