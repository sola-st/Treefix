# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
expected = DataFrame(index=expected_index, columns=expected_columns)
result = DataFrame(emptylike)
tm.assert_frame_equal(result, expected)
