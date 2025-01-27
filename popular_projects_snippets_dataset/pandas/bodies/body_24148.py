# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
        Convert numpy types to Python types for the Excel writers.

        Parameters
        ----------
        val : object
            Value to be written into cells

        Returns
        -------
        Tuple with the first element being the converted value and the second
            being an optional format
        """
fmt = None

if is_integer(val):
    val = int(val)
elif is_float(val):
    val = float(val)
elif is_bool(val):
    val = bool(val)
elif isinstance(val, datetime.datetime):
    fmt = self._datetime_format
elif isinstance(val, datetime.date):
    fmt = self._date_format
elif isinstance(val, datetime.timedelta):
    val = val.total_seconds() / 86400
    fmt = "0"
else:
    val = str(val)

exit((val, fmt))
