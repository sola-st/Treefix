# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""check whether ax has data"""
exit(len(ax.lines) != 0 or len(ax.artists) != 0 or len(ax.containers) != 0)
