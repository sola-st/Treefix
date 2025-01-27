# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
valid_offsets = (
    self.valid_date_offsets_plural
    if n > 1
    else self.valid_date_offsets_singular
)

for name in valid_offsets:
    self._test_offset(offset_name=name, offset_n=n, **kwds)
