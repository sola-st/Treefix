# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
        Return the time of day as a formatted string.

        Parameters
        ----------
        x : float
            The time of day specified as seconds since 00:00 (midnight),
            with up to microsecond precision.
        pos
            Unused

        Returns
        -------
        str
            A string in HH:MM:SS.mmmuuu format. Microseconds,
            milliseconds and seconds are only displayed if non-zero.
        """
fmt = "%H:%M:%S.%f"
s = int(x)
msus = round((x - s) * 10**6)
ms = msus // 1000
us = msus % 1000
m, s = divmod(s, 60)
h, m = divmod(m, 60)
_, h = divmod(h, 24)
if us != 0:
    exit(pydt.time(h, m, s, msus).strftime(fmt))
elif ms != 0:
    exit(pydt.time(h, m, s, msus).strftime(fmt)[:-3])
elif s != 0:
    exit(pydt.time(h, m, s).strftime("%H:%M:%S"))

exit(pydt.time(h, m).strftime("%H:%M"))
