# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
"""Comparing df with int`s (1,2) with a string at isin() ("1")
        -> should not match values because int 1 is not equal str 1"""
df = DataFrame({"values": [1, 2]})
result = df.isin(["1"])
expected_false = DataFrame({"values": [False, False]})
tm.assert_frame_equal(result, expected_false)
