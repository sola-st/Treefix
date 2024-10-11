# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_round.py
# GH#11763
# Here's the test frame we'll be working with
df = DataFrame({"col1": [1.123, 2.123, 3.123], "col2": [1.234, 2.234, 3.234]})

# Default round to integer (i.e. decimals=0)
expected_rounded = DataFrame({"col1": [1.0, 2.0, 3.0], "col2": [1.0, 2.0, 3.0]})
tm.assert_frame_equal(round(df), expected_rounded)
