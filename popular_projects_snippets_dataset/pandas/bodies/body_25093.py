# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
if self.ind is None:
    # np.nanmax() and np.nanmin() ignores the missing values
    sample_range = np.nanmax(y) - np.nanmin(y)
    ind = np.linspace(
        np.nanmin(y) - 0.5 * sample_range,
        np.nanmax(y) + 0.5 * sample_range,
        1000,
    )
elif is_integer(self.ind):
    sample_range = np.nanmax(y) - np.nanmin(y)
    ind = np.linspace(
        np.nanmin(y) - 0.5 * sample_range,
        np.nanmax(y) + 0.5 * sample_range,
        self.ind,
    )
else:
    ind = self.ind
exit(ind)
