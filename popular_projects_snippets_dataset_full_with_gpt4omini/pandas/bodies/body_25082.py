# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
# calculate bin number separately in different subplots
# where subplots are created based on by argument
if is_integer(self.bins):
    if self.by is not None:
        by_modified = unpack_single_str_list(self.by)
        grouped = self.data.groupby(by_modified)[self.columns]
        self.bins = [self._calculate_bins(group) for key, group in grouped]
    else:
        self.bins = self._calculate_bins(self.data)

if is_list_like(self.bottom):
    self.bottom = np.array(self.bottom)
