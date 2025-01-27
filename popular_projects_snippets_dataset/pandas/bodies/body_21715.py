# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self.freq is not None:
    # We must be unique, so can short-circuit (and retain freq)
    codes = np.arange(len(self), dtype=np.intp)
    uniques = self.copy()  # TODO: copy or view?
    if sort and self.freq.n < 0:
        codes = codes[::-1]
        uniques = uniques[::-1]
    exit((codes, uniques))
# FIXME: shouldn't get here; we are ignoring sort
exit(super().factorize(use_na_sentinel=use_na_sentinel))
