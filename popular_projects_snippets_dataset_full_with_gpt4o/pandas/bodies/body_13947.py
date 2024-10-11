# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH: 24980
s = Series(input_array).to_string(index=False)
assert s == expected
