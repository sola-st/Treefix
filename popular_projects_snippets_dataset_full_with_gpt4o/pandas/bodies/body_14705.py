# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py

axes = df.plot(
    kind=kind,
    stacked=stacked,
    subplots=subplots,
    align=align,
    width=width,
    position=position,
    grid=True,
)

axes = self._flatten_visible(axes)

for ax in axes:
    if kind == "bar":
        axis = ax.xaxis
        ax_min, ax_max = ax.get_xlim()
        min_edge = min(p.get_x() for p in ax.patches)
        max_edge = max(p.get_x() + p.get_width() for p in ax.patches)
    elif kind == "barh":
        axis = ax.yaxis
        ax_min, ax_max = ax.get_ylim()
        min_edge = min(p.get_y() for p in ax.patches)
        max_edge = max(p.get_y() + p.get_height() for p in ax.patches)
    else:
        raise ValueError

    # GH 7498
    # compare margins between lim and bar edges
    tm.assert_almost_equal(ax_min, min_edge - 0.25)
    tm.assert_almost_equal(ax_max, max_edge + 0.25)

    p = ax.patches[0]
    if kind == "bar" and (stacked is True or subplots is True):
        edge = p.get_x()
        center = edge + p.get_width() * position
    elif kind == "bar" and stacked is False:
        center = p.get_x() + p.get_width() * len(df.columns) * position
        edge = p.get_x()
    elif kind == "barh" and (stacked is True or subplots is True):
        center = p.get_y() + p.get_height() * position
        edge = p.get_y()
    elif kind == "barh" and stacked is False:
        center = p.get_y() + p.get_height() * len(df.columns) * position
        edge = p.get_y()
    else:
        raise ValueError

    # Check the ticks locates on integer
    assert (axis.get_ticklocs() == np.arange(len(df))).all()

    if align == "center":
        # Check whether the bar locates on center
        tm.assert_almost_equal(axis.get_ticklocs()[0], center)
    elif align == "edge":
        # Check whether the bar's edge starts from the tick
        tm.assert_almost_equal(axis.get_ticklocs()[0], edge)
    else:
        raise ValueError

exit(axes)
