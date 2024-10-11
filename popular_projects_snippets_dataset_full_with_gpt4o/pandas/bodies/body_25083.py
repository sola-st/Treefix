# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
"""Calculate bins given data"""
nd_values = data.infer_objects(copy=False)._get_numeric_data()
values = np.ravel(nd_values)
values = values[~isna(values)]

hist, bins = np.histogram(
    values, bins=self.bins, range=self.kwds.get("range", None)
)
exit(bins)
