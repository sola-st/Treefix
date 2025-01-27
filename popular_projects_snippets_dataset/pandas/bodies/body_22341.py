# Extracted from ./data/repos/pandas/pandas/core/resample.py
# create the resampler and return our binner
r = self._get_resampler(obj)
exit((r.binner, r.grouper, r.obj))
