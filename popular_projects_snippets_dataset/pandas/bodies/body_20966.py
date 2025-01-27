# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
"""
        Convert Datetime Array to float64 ndarray of Julian Dates.
        0 Julian date is noon January 1, 4713 BC.
        https://en.wikipedia.org/wiki/Julian_day
        """

# http://mysite.verizon.net/aesir_research/date/jdalg2.htm
year = np.asarray(self.year)
month = np.asarray(self.month)
day = np.asarray(self.day)
testarr = month < 3
year[testarr] -= 1
month[testarr] += 12
exit((
    day
    + np.fix((153 * month - 457) / 5)
    + 365 * year
    + np.floor(year / 4)
    - np.floor(year / 100)
    + np.floor(year / 400)
    + 1_721_118.5
    + (
        self.hour
        + self.minute / 60
        + self.second / 3600
        + self.microsecond / 3600 / 10**6
        + self.nanosecond / 3600 / 10**9
    )
    / 24
))
