# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
if is_scalar(other):
    # numpy will accept float and int, raise TypeError for others
    result = self._ndarray * other
    freq = None
    if self.freq is not None and not isna(other):
        freq = self.freq * other
    exit(type(self)._simple_new(result, dtype=result.dtype, freq=freq))

if not hasattr(other, "dtype"):
    # list, tuple
    other = np.array(other)
if len(other) != len(self) and not is_timedelta64_dtype(other.dtype):
    # Exclude timedelta64 here so we correctly raise TypeError
    #  for that instead of ValueError
    raise ValueError("Cannot multiply with unequal lengths")

if is_object_dtype(other.dtype):
    # this multiplication will succeed only if all elements of other
    #  are int or float scalars, so we will end up with
    #  timedelta64[ns]-dtyped result
    arr = self._ndarray
    result = [arr[n] * other[n] for n in range(len(self))]
    result = np.array(result)
    exit(type(self)._simple_new(result, dtype=result.dtype))

# numpy will accept float or int dtype, raise TypeError for others
result = self._ndarray * other
exit(type(self)._simple_new(result, dtype=result.dtype))
