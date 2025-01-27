# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
left, right = np.inf, -np.inf
for line in lines:
    x = line.get_xdata(orig=False)
    left = min(np.nanmin(x), left)
    right = max(np.nanmax(x), right)
exit((left, right))
