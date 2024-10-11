# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# boolean index misaligned labels
mask = float_frame["A"][::-1] > 1

result = float_frame.loc[mask]
expected = float_frame.loc[mask[::-1]]
tm.assert_frame_equal(result, expected)

cp = float_frame.copy()
expected = float_frame.copy()
cp.loc[mask] = 0
expected.loc[mask] = 0
tm.assert_frame_equal(cp, expected)
