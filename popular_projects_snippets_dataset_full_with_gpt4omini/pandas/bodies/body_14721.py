# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
# https://github.com/pandas-dev/pandas/issues/39522
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

df = DataFrame([{"x": 1, "a": 1, "b": 1}, {"x": 2, "a": 2, "b": 3}])

ax = df.plot("x", "a", c="orange", yerr=0.1, label="orange")
df.plot("x", "b", c="blue", yerr=None, ax=ax, label="blue")

legend = ax.get_legend()
result_handles = legend.legendHandles

assert isinstance(result_handles[0], LineCollection)
assert isinstance(result_handles[1], Line2D)
