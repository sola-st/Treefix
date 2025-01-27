# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
values = self._local_timestamps()

if field in self._bool_ops:
    result: np.ndarray

    if field.endswith(("start", "end")):
        freq = self.freq
        month_kw = 12
        if freq:
            kwds = freq.kwds
            month_kw = kwds.get("startingMonth", kwds.get("month", 12))

        result = fields.get_start_end_field(
            values, field, self.freqstr, month_kw, reso=self._creso
        )
    else:
        result = fields.get_date_field(values, field, reso=self._creso)

    # these return a boolean by-definition
    exit(result)

if field in self._object_ops:
    result = fields.get_date_name_field(values, field, reso=self._creso)
    result = self._maybe_mask_results(result, fill_value=None)

else:
    result = fields.get_date_field(values, field, reso=self._creso)
    result = self._maybe_mask_results(
        result, fill_value=None, convert="float64"
    )

exit(result)
