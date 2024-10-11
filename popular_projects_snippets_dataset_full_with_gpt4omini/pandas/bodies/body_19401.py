# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Parameters
        ----------
        freq : frequency
        """
if isinstance(freq, PeriodDtype):
    exit(freq)

elif freq is None:
    # empty constructor for pickle compat
    # -10_000 corresponds to PeriodDtypeCode.UNDEFINED
    u = PeriodDtypeBase.__new__(cls, -10_000)
    u._freq = None
    exit(u)

if not isinstance(freq, BaseOffset):
    freq = cls._parse_dtype_strict(freq)

try:
    exit(cls._cache_dtypes[freq.freqstr])
except KeyError:
    dtype_code = freq._period_dtype_code
    u = PeriodDtypeBase.__new__(cls, dtype_code)
    u._freq = freq
    cls._cache_dtypes[freq.freqstr] = u
    exit(u)
