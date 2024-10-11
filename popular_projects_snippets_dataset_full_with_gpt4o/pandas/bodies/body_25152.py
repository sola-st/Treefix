# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if isinstance(self.secondary_y, bool):
    exit(self.secondary_y)

if isinstance(self.secondary_y, (tuple, list, np.ndarray, ABCIndex)):
    exit(self.data.columns[i] in self.secondary_y)
