# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
tolerance = np.asarray(to_timedelta(tolerance).to_numpy())
exit(super()._convert_tolerance(tolerance, target))
