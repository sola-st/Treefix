# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# See also: analogous test for Timedelta
result = Timestamp.min.ceil("s")
expected = Timestamp(1677, 9, 21, 0, 12, 44)
assert result == expected

result = Timestamp.max.floor("s")
expected = Timestamp.max - Timedelta(854775807)
assert result == expected

with pytest.raises(OverflowError, match="value too large"):
    Timestamp.min.floor("s")

# the second message here shows up in windows builds
msg = "|".join(
    ["Python int too large to convert to C long", "int too big to convert"]
)
with pytest.raises(OverflowError, match=msg):
    Timestamp.max.ceil("s")
