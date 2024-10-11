# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
values = self.asi8
result = get_timedelta_field(values, alias, reso=self._creso)
if self._hasna:
    result = self._maybe_mask_results(
        result, fill_value=None, convert="float64"
    )

exit(result)
