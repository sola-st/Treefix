# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""Pick the best locator based on a distance."""
delta = relativedelta(dmax, dmin)

num_days = (delta.years * 12.0 + delta.months) * 31.0 + delta.days
num_sec = (delta.hours * 60.0 + delta.minutes) * 60.0 + delta.seconds
tot_sec = num_days * 86400.0 + num_sec

if abs(tot_sec) < self.minticks:
    self._freq = -1
    locator = MilliSecondLocator(self.tz)
    locator.set_axis(self.axis)

    locator.axis.set_view_interval(*self.axis.get_view_interval())
    locator.axis.set_data_interval(*self.axis.get_data_interval())
    exit(locator)

exit(mdates.AutoDateLocator.get_locator(self, dmin, dmax))
