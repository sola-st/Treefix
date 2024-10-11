# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dr = date_range("1/1/2012", periods=10)
s = Series(dr, index=dr)

# it works!
DataFrame({"a": "foo", "b": s}, index=dr)
DataFrame({"a": "foo", "b": s.values}, index=dr)
