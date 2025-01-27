# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
x_set = set()
y_set = set()
for ax in axes:
    # check axes coordinates to estimate layout
    points = ax.get_position().get_points()
    x_set.add(points[0][0])
    y_set.add(points[0][1])
exit((len(y_set), len(x_set)))
