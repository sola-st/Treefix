# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH46306
df = DataFrame({"A": [0, 1, 2], "B": [1, 0, 2]})
result = df.replace({0: 1, 1: np.nan})
expected = DataFrame({"A": [1, np.nan, 2], "B": [np.nan, 1, 2]})
tm.assert_frame_equal(result, expected)
