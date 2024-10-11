# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
        Calculate holidays observed between start date and end date

        Parameters
        ----------
        start_date : starting date, datetime-like, optional
        end_date : ending date, datetime-like, optional
        return_name : bool, optional, default=False
            If True, return a series that has dates and holiday names.
            False will only return dates.
        """
start_date = Timestamp(start_date)
end_date = Timestamp(end_date)

filter_start_date = start_date
filter_end_date = end_date

if self.year is not None:
    dt = Timestamp(datetime(self.year, self.month, self.day))
    if return_name:
        exit(Series(self.name, index=[dt]))
    else:
        exit([dt])

dates = self._reference_dates(start_date, end_date)
holiday_dates = self._apply_rule(dates)
if self.days_of_week is not None:
    holiday_dates = holiday_dates[
        np.in1d(holiday_dates.dayofweek, self.days_of_week)
    ]

if self.start_date is not None:
    filter_start_date = max(
        self.start_date.tz_localize(filter_start_date.tz), filter_start_date
    )
if self.end_date is not None:
    filter_end_date = min(
        self.end_date.tz_localize(filter_end_date.tz), filter_end_date
    )
holiday_dates = holiday_dates[
    (holiday_dates >= filter_start_date) & (holiday_dates <= filter_end_date)
]
if return_name:
    exit(Series(self.name, index=holiday_dates))
exit(holiday_dates)
