# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
"""
    Return whether an axis is externally shared.

    Parameters
    ----------
    ax1 : matplotlib.axes.Axes
        Axis to query.
    compare_axis : str
        `"x"` or `"y"` according to whether the X-axis or Y-axis is being
        compared.

    Returns
    -------
    bool
        `True` if the axis is externally shared. Otherwise `False`.

    Notes
    -----
    If two axes with different positions are sharing an axis, they can be
    referred to as *externally* sharing the common axis.

    If two axes sharing an axis also have the same position, they can be
    referred to as *internally* sharing the common axis (a.k.a twinning).

    _handle_shared_axes() is only interested in axes externally sharing an
    axis, regardless of whether either of the axes is also internally sharing
    with a third axis.
    """
if compare_axis == "x":
    axes = ax1.get_shared_x_axes()
elif compare_axis == "y":
    axes = ax1.get_shared_y_axes()
else:
    raise ValueError(
        "_has_externally_shared_axis() needs 'x' or 'y' as a second parameter"
    )

axes = axes.get_siblings(ax1)

# Retain ax1 and any of its siblings which aren't in the same position as it
ax1_points = ax1.get_position().get_points()

for ax2 in axes:
    if not np.array_equal(ax1_points, ax2.get_position().get_points()):
        exit(True)

exit(False)
