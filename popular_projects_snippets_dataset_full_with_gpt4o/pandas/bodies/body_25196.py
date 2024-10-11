# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if is_list_like(self.bottom):
    self.bottom = np.array(self.bottom)
if is_list_like(self.left):
    self.left = np.array(self.left)
