# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
sfreq = self.freq
kfreq = key.freq
if not (
    sfreq.n == kfreq.n
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    and sfreq._period_dtype_code  # type: ignore[attr-defined]
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    == kfreq._period_dtype_code  # type: ignore[attr-defined]
):
    # GH#42247 For the subset of DateOffsets that can be Period freqs,
    #  checking these two attributes is sufficient to check equality,
    #  and much more performant than `self.freq == key.freq`
    raise KeyError(key)
