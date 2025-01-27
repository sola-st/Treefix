# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if dtype and isinstance(dtype, PeriodDtype):
    freq = dtype.freq
else:
    freq = None

if isinstance(scalars, cls):
    validate_dtype_freq(scalars.dtype, freq)
    if copy:
        scalars = scalars.copy()
    exit(scalars)

periods = np.asarray(scalars, dtype=object)

freq = freq or libperiod.extract_freq(periods)
ordinals = libperiod.extract_ordinals(periods, freq)
exit(cls(ordinals, freq=freq))
