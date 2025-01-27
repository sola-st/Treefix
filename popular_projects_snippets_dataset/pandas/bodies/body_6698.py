# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# Has float subtype if any of start/end/freq are float, even if all
# resulting endpoints can safely be upcast to integers

# defined from start/end/freq
index = interval_range(start=start, end=end, freq=freq)
result = index.dtype.subtype
expected = "int64" if is_integer(start + end + freq) else "float64"
assert result == expected

# defined from start/periods/freq
index = interval_range(start=start, periods=5, freq=freq)
result = index.dtype.subtype
expected = "int64" if is_integer(start + freq) else "float64"
assert result == expected

# defined from end/periods/freq
index = interval_range(end=end, periods=5, freq=freq)
result = index.dtype.subtype
expected = "int64" if is_integer(end + freq) else "float64"
assert result == expected

# GH 20976: linspace behavior defined from start/end/periods
index = interval_range(start=start, end=end, periods=5)
result = index.dtype.subtype
expected = "int64" if is_integer(start + end) else "float64"
assert result == expected
