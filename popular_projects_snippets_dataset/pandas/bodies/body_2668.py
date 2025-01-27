# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_round.py
# GH#30063
columns = pd.CategoricalIndex(pd.interval_range(0, 2))
df = DataFrame([[0.66, 1.1], [0.3, 0.25]], columns=columns)

result = df.round()
expected = DataFrame([[1.0, 1.0], [0.0, 0.0]], columns=columns)
tm.assert_frame_equal(result, expected)
