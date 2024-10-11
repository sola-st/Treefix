# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# See also: analogous test for Timestamp
# GH#38964
result = Timedelta.min.ceil("s")
expected = Timedelta.min + Timedelta(seconds=1) - Timedelta(145224193)
assert result == expected

result = Timedelta.max.floor("s")
expected = Timedelta.max - Timedelta(854775807)
assert result == expected

with pytest.raises(OverflowError, match="value too large"):
    Timedelta.min.floor("s")

# the second message here shows up in windows builds
msg = "|".join(
    ["Python int too large to convert to C long", "int too big to convert"]
)
with pytest.raises(OverflowError, match=msg):
    Timedelta.max.ceil("s")
