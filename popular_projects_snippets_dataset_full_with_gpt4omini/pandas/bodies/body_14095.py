# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# Issue #23614
df = DataFrame({"A": [6.0, 3.1, 2.2]})
expected = "     A\n0  6,0\n1  3,1\n2  2,2"
assert df.to_string(decimal=",") == expected
