# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
if hrs_offset >= 0:
    offset_string = f"{hrs_offset:02d}00"
else:
    offset_string = f"-{(hrs_offset * -1):02}00"
exit(Timestamp(string + offset_string).tz_convert(tz))
