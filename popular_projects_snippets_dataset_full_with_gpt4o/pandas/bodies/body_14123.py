# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
ts = tm.makeTimeSeries()
buf = StringIO()

s = ts.to_string()

retval = ts.to_string(buf=buf)
assert retval is None
assert buf.getvalue().strip() == s

# pass float_format
format = "%.4f".__mod__
result = ts.to_string(float_format=format)
result = [x.split()[1] for x in result.split("\n")[:-1]]
expected = [format(x) for x in ts]
assert result == expected

# empty string
result = ts[:0].to_string()
assert result == "Series([], Freq: B)"

result = ts[:0].to_string(length=0)
assert result == "Series([], Freq: B)"

# name and length
cp = ts.copy()
cp.name = "foo"
result = cp.to_string(length=True, name=True, dtype=True)
last_line = result.split("\n")[-1].strip()
assert last_line == (f"Freq: B, Name: foo, Length: {len(cp)}, dtype: float64")
