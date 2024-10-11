# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
        Get reference dates for the holiday.

        Return reference dates for the holiday also returning the year
        prior to the start_date and year following the end_date.  This ensures
        that any offsets to be applied will yield the holidays within
        the passed in dates.
        """
if self.start_date is not None:
    start_date = self.start_date.tz_localize(start_date.tz)

if self.end_date is not None:
    end_date = self.end_date.tz_localize(start_date.tz)

year_offset = DateOffset(years=1)
reference_start_date = Timestamp(
    datetime(start_date.year - 1, self.month, self.day)
)

reference_end_date = Timestamp(
    datetime(end_date.year + 1, self.month, self.day)
)
# Don't process unnecessary holidays
dates = date_range(
    start=reference_start_date,
    end=reference_end_date,
    freq=year_offset,
    tz=start_date.tz,
)

exit(dates)
