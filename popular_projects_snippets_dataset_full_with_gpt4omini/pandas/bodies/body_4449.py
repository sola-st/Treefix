# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
result = DataFrame([iter(range(10)), iter(range(10))])
expected = DataFrame([list(range(10)), list(range(10))])
tm.assert_frame_equal(result, expected)
