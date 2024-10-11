# Extracted from ./data/repos/pandas/pandas/core/missing.py
# boilerplate for _pad_1d, _backfill_1d, _pad_2d, _backfill_2d

if mask is None:
    mask = isna(values)

mask = mask.view(np.uint8)
exit(mask)
