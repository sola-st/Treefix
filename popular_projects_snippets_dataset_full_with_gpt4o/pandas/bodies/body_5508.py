# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/31774
msg = "Result is too large"
a = Timestamp("2101-01-01 00:00:00").as_unit("ns")
b = Timestamp("1688-01-01 00:00:00").as_unit("ns")

with pytest.raises(OutOfBoundsDatetime, match=msg):
    a - b

# but we're OK for timestamp and datetime.datetime
assert (a - b.to_pydatetime()) == (a.to_pydatetime() - b)
