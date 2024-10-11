# Extracted from ./data/repos/pandas/pandas/core/generic.py
axis = self._get_axis_number(axis)

if win_type is not None:
    exit(Window(
        self,
        window=window,
        min_periods=min_periods,
        center=center,
        win_type=win_type,
        on=on,
        axis=axis,
        closed=closed,
        step=step,
        method=method,
    ))

exit(Rolling(
    self,
    window=window,
    min_periods=min_periods,
    center=center,
    win_type=win_type,
    on=on,
    axis=axis,
    closed=closed,
    step=step,
    method=method,
))
