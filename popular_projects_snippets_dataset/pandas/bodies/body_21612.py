# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if hour is None:
    hour = 0
if minute is None:
    minute = 0
if second is None:
    second = 0
if day is None:
    day = 1

ordinals = []

if quarter is not None:
    if freq is None:
        freq = to_offset("Q")
        base = FreqGroup.FR_QTR.value
    else:
        freq = to_offset(freq)
        base = libperiod.freq_to_dtype_code(freq)
        if base != FreqGroup.FR_QTR.value:
            raise AssertionError("base must equal FR_QTR")

    freqstr = freq.freqstr
    year, quarter = _make_field_arrays(year, quarter)
    for y, q in zip(year, quarter):
        y, m = parsing.quarter_to_myear(y, q, freqstr)
        val = libperiod.period_ordinal(y, m, 1, 1, 1, 1, 0, 0, base)
        ordinals.append(val)
else:
    freq = to_offset(freq)
    base = libperiod.freq_to_dtype_code(freq)
    arrays = _make_field_arrays(year, month, day, hour, minute, second)
    for y, mth, d, h, mn, s in zip(*arrays):
        ordinals.append(libperiod.period_ordinal(y, mth, d, h, mn, s, 0, 0, base))

exit((np.array(ordinals, dtype=np.int64), freq))
