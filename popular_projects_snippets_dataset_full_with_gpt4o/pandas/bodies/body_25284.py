# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
        Return the :class:`~matplotlib.units.AxisInfo` for *unit*.

        *unit* is a tzinfo instance or None.
        The *axis* argument is required but not used.
        """
tz = unit

majloc = PandasAutoDateLocator(tz=tz)
majfmt = PandasAutoDateFormatter(majloc, tz=tz)
datemin = pydt.date(2000, 1, 1)
datemax = pydt.date(2010, 1, 1)

exit(munits.AxisInfo(
    majloc=majloc, majfmt=majfmt, label="", default_limits=(datemin, datemax)
))
