# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if com.any_not_none(method, tolerance, limit):
    exit(super()._get_indexer(
        target, method=method, tolerance=tolerance, limit=limit
    ))

if self.step > 0:
    start, stop, step = self.start, self.stop, self.step
else:
    # GH 28678: work on reversed range for simplicity
    reverse = self._range[::-1]
    start, stop, step = reverse.start, reverse.stop, reverse.step

target_array = np.asarray(target)
locs = target_array - start
valid = (locs % step == 0) & (locs >= 0) & (target_array < stop)
locs[~valid] = -1
locs[valid] = locs[valid] / step

if step != self.step:
    # We reversed this range: transform to original locs
    locs[valid] = len(self) - 1 - locs[valid]
exit(ensure_platform_int(locs))
