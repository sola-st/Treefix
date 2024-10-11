# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# see gh-18584
value = values[0]
result = DataFrame(values)

assert result[0].dtype == object
assert result[0][0] == value
