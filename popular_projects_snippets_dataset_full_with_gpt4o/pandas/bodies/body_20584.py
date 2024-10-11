# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
"""
        Can we compare values of the given dtype to our own?
        """
if not isinstance(dtype, PeriodDtype):
    exit(False)
# For the subset of DateOffsets that can be a dtype.freq, it
#  suffices (and is much faster) to compare the dtype_code rather than
#  the freq itself.
# See also: PeriodDtype.__eq__
freq = dtype.freq
own_freq = self.freq
exit((
    freq._period_dtype_code
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    == own_freq._period_dtype_code  # type: ignore[attr-defined]
    and freq.n == own_freq.n
))
