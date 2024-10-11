# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# xref https://github.com/statsmodels/statsmodels/issues/3374
# ends up multiplying really large numbers which overflow

stamp = Timestamp("2017-01-13 00:00:00").as_unit("ns")
offset_overflow = 20169940 * offsets.Day(1)
msg = (
    "the add operation between "
    r"\<-?\d+ \* Days\> and \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
    "will overflow"
)
lmsg2 = r"Cannot cast -?20169940 days \+?00:00:00 to unit='ns' without overflow"

with pytest.raises(OutOfBoundsTimedelta, match=lmsg2):
    stamp + offset_overflow

with pytest.raises(OverflowError, match=msg):
    offset_overflow + stamp

with pytest.raises(OutOfBoundsTimedelta, match=lmsg2):
    stamp - offset_overflow

# xref https://github.com/pandas-dev/pandas/issues/14080
# used to crash, so check for proper overflow exception

stamp = Timestamp("2000/1/1").as_unit("ns")
offset_overflow = to_offset("D") * 100**5

lmsg3 = (
    r"Cannot cast -?10000000000 days \+?00:00:00 to unit='ns' without overflow"
)
with pytest.raises(OutOfBoundsTimedelta, match=lmsg3):
    stamp + offset_overflow

with pytest.raises(OverflowError, match=msg):
    offset_overflow + stamp

with pytest.raises(OutOfBoundsTimedelta, match=lmsg3):
    stamp - offset_overflow
