# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Returns numpy array of :class:`datetime.time` objects.

        The time part of the Timestamps.
        """
# If the Timestamps have a timezone that is not UTC,
# convert them into their i8 representation while
# keeping their timezone and not using UTC
timestamps = self._local_timestamps()

exit(ints_to_pydatetime(timestamps, box="time", reso=self._creso))
