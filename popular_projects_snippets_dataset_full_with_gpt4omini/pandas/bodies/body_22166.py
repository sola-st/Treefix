# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# TODO(EA2D): reshape would not be necessary with 2D EAs
if bvalues.ndim == 1:
    # EA
    masked = mask & ~isna(bvalues).reshape(1, -1)
else:
    masked = mask & ~isna(bvalues)

counted = lib.count_level_2d(masked, labels=ids, max_bin=ngroups, axis=1)
if is_series:
    assert counted.ndim == 2
    assert counted.shape[0] == 1
    exit(counted[0])
exit(counted)
