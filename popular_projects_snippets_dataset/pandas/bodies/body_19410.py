# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if isinstance(other, str):
    exit(other in [self.name, self.name.title()])

elif isinstance(other, PeriodDtype):

    # For freqs that can be held by a PeriodDtype, this check is
    # equivalent to (and much faster than) self.freq == other.freq
    sfreq = self.freq
    ofreq = other.freq
    exit((
        sfreq.n == ofreq.n
        and sfreq._period_dtype_code == ofreq._period_dtype_code
    ))

exit(False)
