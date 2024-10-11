# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
"""
    Context manager for temporarily setting a timezone.

    Parameters
    ----------
    tz : str
        A string representing a valid timezone.

    Examples
    --------
    >>> from datetime import datetime
    >>> from dateutil.tz import tzlocal
    >>> tzlocal().tzname(datetime(2021, 1, 1))  # doctest: +SKIP
    'IST'

    >>> with set_timezone('US/Eastern'):
    ...     tzlocal().tzname(datetime(2021, 1, 1))
    ...
    'EST'
    """
import time

def setTZ(tz) -> None:
    if tz is None:
        try:
            del os.environ["TZ"]
        except KeyError:
            pass
    else:
        os.environ["TZ"] = tz
        time.tzset()

orig_tz = os.environ.get("TZ")
setTZ(tz)
try:
    exit()
finally:
    setTZ(orig_tz)
