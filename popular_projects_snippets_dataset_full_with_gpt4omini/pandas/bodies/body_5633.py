# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
"""Comparing df with floats (1.4245,2.32441) with a string at isin() ("1.4245")
        -> should not match values because float 1.4245 is not equal str 1.4245"""
df = DataFrame({"values": [1.4245, 2.32441]})
result = df.isin(["1.4245"])
expected_false = DataFrame({"values": [False, False]})
tm.assert_frame_equal(result, expected_false)
