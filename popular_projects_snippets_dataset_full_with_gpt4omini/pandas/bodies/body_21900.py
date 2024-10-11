# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
additional_nans = np.array([np.nan] * offset)
x = np.concatenate((x, additional_nans))
exit(func(x, window, self.min_periods or len(window)))
