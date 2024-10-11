# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

result = DataFrame([{}])
expected = DataFrame(index=RangeIndex(1), columns=[])
tm.assert_frame_equal(result, expected)
