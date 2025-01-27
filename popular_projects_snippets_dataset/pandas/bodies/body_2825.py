# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/12392
df = DataFrame({"A": [1, 2, 3], "B": [1, 2, 3]})
result = df.reindex([0, 1], columns=["A"])
expected = DataFrame({"A": [1, 2]})
tm.assert_frame_equal(result, expected)
