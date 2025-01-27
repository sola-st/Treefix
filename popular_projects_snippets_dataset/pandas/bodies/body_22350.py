# Extracted from ./data/repos/pandas/pandas/core/resample.py
# NaT handling as in pandas._lib.lib.generate_bins_dt64()
# shift bins by the number of NaT
assert nat_count > 0
bins += nat_count
bins = np.insert(bins, 0, nat_count)

# Incompatible types in assignment (expression has type "Index", variable
# has type "PeriodIndex")
binner = binner.insert(0, NaT)  # type: ignore[assignment]
# Incompatible types in assignment (expression has type "Index", variable
# has type "PeriodIndex")
labels = labels.insert(0, NaT)  # type: ignore[assignment]
exit((binner, bins, labels))
