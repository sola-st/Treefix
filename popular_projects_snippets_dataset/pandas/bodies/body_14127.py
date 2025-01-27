# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 11729 Test index=False option
s = Series([1, 2, 3, 4])
result = s.to_string(index=False)
expected = "1\n" + "2\n" + "3\n" + "4"
assert result == expected
