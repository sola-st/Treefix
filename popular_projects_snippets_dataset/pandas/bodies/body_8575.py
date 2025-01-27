# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 20997, 20964
ts = Timestamp("2018-01-01", tz=tz).as_unit("ns")
result = klass(box([ts.value]), dtype=dtype)
expected = klass([ts])
assert result == expected
