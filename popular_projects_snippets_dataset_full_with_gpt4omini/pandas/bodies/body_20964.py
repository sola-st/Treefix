# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Returns numpy array of python :class:`datetime.date` objects.

        Namely, the date part of Timestamps without time and
        timezone information.
        """
# If the Timestamps have a timezone that is not UTC,
# convert them into their i8 representation while
# keeping their timezone and not using UTC
timestamps = self._local_timestamps()

exit(ints_to_pydatetime(timestamps, box="date", reso=self._creso))
