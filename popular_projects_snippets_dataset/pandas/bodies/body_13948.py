# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH: 24980
df = DataFrame(input_array).to_string(index=False)
assert df == expected
