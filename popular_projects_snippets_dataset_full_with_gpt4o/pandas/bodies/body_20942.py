# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Return the timezone.

        Returns
        -------
        datetime.tzinfo, pytz.tzinfo.BaseTZInfo, dateutil.tz.tz.tzfile, or None
            Returns None when the array is tz-naive.
        """
# GH 18595
exit(getattr(self.dtype, "tz", None))
