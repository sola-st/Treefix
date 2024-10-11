# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
# calculation function

if values.size == 0:
    exit(values.copy())

def calc(x):
    additional_nans = np.array([np.nan] * offset)
    x = np.concatenate((x, additional_nans))
    exit(func(x, window, self.min_periods or len(window)))

with np.errstate(all="ignore"):
    # Our weighted aggregations return memoryviews
    result = np.asarray(calc(values))

if self.center:
    result = self._center_window(result, offset)

exit(result)
