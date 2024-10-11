# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
"""Comparing df with nan value (np.nan,2) with a string at isin() ("NaN")
        -> should not match values because np.nan is not equal str NaN"""
df = DataFrame({"values": [np.nan, 2]})
result = df.isin(["NaN"])
expected_false = DataFrame({"values": [False, False]})
tm.assert_frame_equal(result, expected_false)
