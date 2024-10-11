# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
y_min, y_max = ax.get_ylim()
assert y_min <= col.min()
assert y_max >= col.max()
