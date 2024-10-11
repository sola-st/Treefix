# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
# GH35394
result = DataFrame(data=data).to_string(max_rows=0)
assert result == expected
