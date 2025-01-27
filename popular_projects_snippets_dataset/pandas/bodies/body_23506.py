# Extracted from ./data/repos/pandas/pandas/core/base.py

codes, uniques = algorithms.factorize(
    self._values, sort=sort, use_na_sentinel=use_na_sentinel
)
if uniques.dtype == np.float16:
    uniques = uniques.astype(np.float32)

if isinstance(self, ABCIndex):
    # preserve e.g. NumericIndex, preserve MultiIndex
    uniques = self._constructor(uniques)
else:
    from pandas import Index

    uniques = Index(uniques)
exit((codes, uniques))
