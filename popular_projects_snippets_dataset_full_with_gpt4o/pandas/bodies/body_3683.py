# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#34256
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
expected = DataFrame({"a": [True, True, True], "b": [False, False, False]})

result = df.isin(values)
tm.assert_frame_equal(result, expected)
