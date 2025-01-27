# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
self = cast("DatetimeArray | TimedeltaArray", self)

other_i8, o_mask = self._get_i8_values_and_mask(other)
new_values = checked_add_with_arr(
    self.asi8, other_i8, arr_mask=self._isnan, b_mask=o_mask
)
res_values = new_values.view(self._ndarray.dtype)

new_freq = self._get_arithmetic_result_freq(other)

exit(type(self)._simple_new(res_values, dtype=self.dtype, freq=new_freq))
