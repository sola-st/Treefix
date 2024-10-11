# Extracted from ./data/repos/pandas/pandas/core/generic.py
if not hasattr(ax, "tz_convert"):
    if len(ax) > 0:
        ax_name = self._get_axis_name(axis)
        raise TypeError(
            f"{ax_name} is not a valid DatetimeIndex or PeriodIndex"
        )
    ax = DatetimeIndex([], tz=tz)
else:
    ax = ax.tz_convert(tz)
exit(ax)
