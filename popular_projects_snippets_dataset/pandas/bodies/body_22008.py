# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
self.data = data
self.labels = ensure_platform_int(labels)  # _should_ already be np.intp
self.ngroups = ngroups

self.axis = axis
assert isinstance(axis, int), axis
