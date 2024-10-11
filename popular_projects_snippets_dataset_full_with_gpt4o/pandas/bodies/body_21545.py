# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if not len(self) or periods == 0:
    exit(self.copy())

if isna(fill_value):
    fill_value = self.dtype.na_value

# ExtensionArray.shift doesn't work for two reasons
# 1. IntervalArray.dtype.na_value may not be correct for the dtype.
# 2. IntervalArray._from_sequence only accepts NaN for missing values,
#    not other values like NaT

empty_len = min(abs(periods), len(self))
if isna(fill_value):
    from pandas import Index

    fill_value = Index(self._left, copy=False)._na_value
    empty = IntervalArray.from_breaks([fill_value] * (empty_len + 1))
else:
    empty = self._from_sequence([fill_value] * empty_len)

if periods > 0:
    a = empty
    b = self[:-periods]
else:
    a = self[abs(periods) :]
    b = empty
exit(self._concat_same_type([a, b]))
