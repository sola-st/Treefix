# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Return my resampler or raise if we have an invalid axis.

        Parameters
        ----------
        obj : input object
        kind : string, optional
            'period','timestamp','timedelta' are valid

        Returns
        -------
        a Resampler

        Raises
        ------
        TypeError if incompatible axis

        """
self._set_grouper(obj)

ax = self.ax
if isinstance(ax, DatetimeIndex):
    exit(DatetimeIndexResampler(
        obj, groupby=self, kind=kind, axis=self.axis, group_keys=self.group_keys
    ))
elif isinstance(ax, PeriodIndex) or kind == "period":
    exit(PeriodIndexResampler(
        obj, groupby=self, kind=kind, axis=self.axis, group_keys=self.group_keys
    ))
elif isinstance(ax, TimedeltaIndex):
    exit(TimedeltaIndexResampler(
        obj, groupby=self, axis=self.axis, group_keys=self.group_keys
    ))

raise TypeError(
    "Only valid with DatetimeIndex, "
    "TimedeltaIndex or PeriodIndex, "
    f"but got an instance of '{type(ax).__name__}'"
)
