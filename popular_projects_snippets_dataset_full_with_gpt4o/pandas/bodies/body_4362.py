# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
expected = DataFrame()
result = constructor()
assert len(result.index) == 0
assert len(result.columns) == 0
tm.assert_frame_equal(result, expected)
