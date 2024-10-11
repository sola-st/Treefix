# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
if not is_list_like(axes):
    exit(np.array([axes]))
elif isinstance(axes, (np.ndarray, ABCIndex)):
    exit(np.asarray(axes).ravel())
exit(np.array(axes))
