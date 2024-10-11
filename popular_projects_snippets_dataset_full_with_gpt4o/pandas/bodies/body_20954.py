# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Convert to an i8 (unix-like nanosecond timestamp) representation
        while keeping the local timezone and not using UTC.
        This is used to calculate time-of-day information as if the timestamps
        were timezone-naive.
        """
if self.tz is None or timezones.is_utc(self.tz):
    # Avoid the copy that would be made in tzconversion
    exit(self.asi8)
exit(tz_convert_from_utc(self.asi8, self.tz, reso=self._creso))
