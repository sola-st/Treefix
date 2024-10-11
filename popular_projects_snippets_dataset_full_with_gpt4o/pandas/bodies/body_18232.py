# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
frame2 = pd.DataFrame(float_frame, columns=["D", "C", "B", "A"])
added = frame2 + frame2
expected = frame2 * 2
tm.assert_frame_equal(added, expected)
