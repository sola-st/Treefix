# Extracted from ./data/repos/pandas/pandas/core/resample.py
# First and last offsets should be calculated from the start day to fix an
# error cause by resampling across multiple days when a one day period is
# not a multiple of the frequency. See GH 8683
# To handle frequencies that are not multiple or divisible by a day we let
# the possibility to define a fixed origin timestamp. See GH 31809
first = first.as_unit("ns")
last = last.as_unit("ns")
if offset is not None:
    offset = offset.as_unit("ns")

origin_nanos = 0  # origin == "epoch"
if origin == "start_day":
    origin_nanos = first.normalize().value
elif origin == "start":
    origin_nanos = first.value
elif isinstance(origin, Timestamp):
    origin_nanos = origin.as_unit("ns").value
elif origin in ["end", "end_day"]:
    origin_last = last if origin == "end" else last.ceil("D")
    sub_freq_times = (origin_last.value - first.value) // freq.nanos
    if closed == "left":
        sub_freq_times += 1
    first = origin_last - sub_freq_times * freq
    origin_nanos = first.value
origin_nanos += offset.value if offset else 0

# GH 10117 & GH 19375. If first and last contain timezone information,
# Perform the calculation in UTC in order to avoid localizing on an
# Ambiguous or Nonexistent time.
first_tzinfo = first.tzinfo
last_tzinfo = last.tzinfo
if first_tzinfo is not None:
    first = first.tz_convert("UTC")
if last_tzinfo is not None:
    last = last.tz_convert("UTC")

foffset = (first.value - origin_nanos) % freq.nanos
loffset = (last.value - origin_nanos) % freq.nanos

if closed == "right":
    if foffset > 0:
        # roll back
        fresult_int = first.value - foffset
    else:
        fresult_int = first.value - freq.nanos

    if loffset > 0:
        # roll forward
        lresult_int = last.value + (freq.nanos - loffset)
    else:
        # already the end of the road
        lresult_int = last.value
else:  # closed == 'left'
    if foffset > 0:
        fresult_int = first.value - foffset
    else:
        # start of the road
        fresult_int = first.value

    if loffset > 0:
        # roll forward
        lresult_int = last.value + (freq.nanos - loffset)
    else:
        lresult_int = last.value + freq.nanos
fresult = Timestamp(fresult_int)
lresult = Timestamp(lresult_int)
if first_tzinfo is not None:
    fresult = fresult.tz_localize("UTC").tz_convert(first_tzinfo)
if last_tzinfo is not None:
    lresult = lresult.tz_localize("UTC").tz_convert(last_tzinfo)
exit((fresult, lresult))
