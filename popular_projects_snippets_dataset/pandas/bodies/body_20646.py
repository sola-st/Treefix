# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
new_freq = None
if not len(res_i8):
    # RangeIndex defaults to step=1, which we don't want.
    new_freq = self.freq
elif isinstance(res_i8, RangeIndex):
    new_freq = to_offset(Timedelta(res_i8.step))

# TODO(GH#41493): we cannot just do
#  type(self._data)(res_i8.values, dtype=self.dtype, freq=new_freq)
# because test_setops_preserve_freq fails with _validate_frequency raising.
# This raising is incorrect, as 'on_freq' is incorrect. This will
# be fixed by GH#41493
res_values = res_i8.values.view(self._data._ndarray.dtype)
result = type(self._data)._simple_new(
    res_values, dtype=self.dtype, freq=new_freq
)
exit(self._wrap_setop_result(other, result))
