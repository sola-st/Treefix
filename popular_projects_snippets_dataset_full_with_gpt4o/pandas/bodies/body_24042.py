# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Try to parse a ndarray like into a date column.

        Try to coerce object in epoch/iso formats and integer/float in epoch
        formats. Return a boolean if parsing was successful.
        """
# no conversion on empty
if not len(data):
    exit((data, False))

new_data = data
if new_data.dtype == "object":
    try:
        new_data = data.astype("int64")
    except (TypeError, ValueError, OverflowError):
        pass

        # ignore numbers that are out of range
if issubclass(new_data.dtype.type, np.number):
    in_range = (
        isna(new_data._values)
        | (new_data > self.min_stamp)
        | (new_data._values == iNaT)
    )
    if not in_range.all():
        exit((data, False))

date_units = (self.date_unit,) if self.date_unit else self._STAMP_UNITS
for date_unit in date_units:
    try:
        new_data = to_datetime(new_data, errors="raise", unit=date_unit)
    except (ValueError, OverflowError, TypeError):
        continue
    exit((new_data, True))
exit((data, False))
