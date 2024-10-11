# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# names match, preserve
result = datetime_series * datetime_series
assert result.name == datetime_series.name
result = datetime_series.mul(datetime_series)
assert result.name == datetime_series.name

result = datetime_series * datetime_series[:-2]
assert result.name == datetime_series.name

# names don't match, don't preserve
cp = datetime_series.copy()
cp.name = "something else"
result = datetime_series + cp
assert result.name is None
result = datetime_series.add(cp)
assert result.name is None

ops = ["add", "sub", "mul", "div", "truediv", "floordiv", "mod", "pow"]
ops = ops + ["r" + op for op in ops]
for op in ops:
    # names match, preserve
    ser = datetime_series.copy()
    result = getattr(ser, op)(ser)
    assert result.name == datetime_series.name

    # names don't match, don't preserve
    cp = datetime_series.copy()
    cp.name = "changed"
    result = getattr(ser, op)(cp)
    assert result.name is None
