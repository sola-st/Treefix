# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Calculate year, week, and day according to the ISO 8601 standard.

        .. versionadded:: 1.1.0

        Returns
        -------
        DataFrame
            With columns year, week and day.

        See Also
        --------
        Timestamp.isocalendar : Function return a 3-tuple containing ISO year,
            week number, and weekday for the given Timestamp object.
        datetime.date.isocalendar : Return a named tuple object with
            three components: year, week and weekday.

        Examples
        --------
        >>> idx = pd.date_range(start='2019-12-29', freq='D', periods=4)
        >>> idx.isocalendar()
                    year  week  day
        2019-12-29  2019    52    7
        2019-12-30  2020     1    1
        2019-12-31  2020     1    2
        2020-01-01  2020     1    3
        >>> idx.isocalendar().week
        2019-12-29    52
        2019-12-30     1
        2019-12-31     1
        2020-01-01     1
        Freq: D, Name: week, dtype: UInt32
        """
from pandas import DataFrame

values = self._local_timestamps()
sarray = fields.build_isocalendar_sarray(values, reso=self._creso)
iso_calendar_df = DataFrame(
    sarray, columns=["year", "week", "day"], dtype="UInt32"
)
if self._hasna:
    iso_calendar_df.iloc[self._isnan] = None
exit(iso_calendar_df)
