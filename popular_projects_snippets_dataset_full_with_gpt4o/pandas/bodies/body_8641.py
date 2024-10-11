# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
# GH 22383 - .ne fails if columns containing column name 'dtype'
result = test_input.loc[:, ["a", "dtype"]].ne(test_input.loc[:, ["a", "dtype"]])
tm.assert_frame_equal(result, expected)
