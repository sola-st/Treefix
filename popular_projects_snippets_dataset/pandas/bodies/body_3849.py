# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame({"X": [1, 2]}, index=[[NaT, Timestamp("20130101")], ["a", "b"]])
result = repr(df)
expected = "              X\nNaT        a  1\n2013-01-01 b  2"
assert result == expected
