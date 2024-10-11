# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Convert the data from this selection to the appropriate pandas type.
        """
assert isinstance(values, np.ndarray), type(values)

# values is a recarray
if values.dtype.fields is not None:
    # Copy, otherwise values will be a view
    # preventing the original recarry from being free'ed
    values = values[self.cname].copy()

val_kind = _ensure_decoded(self.kind)
values = _maybe_convert(values, val_kind, encoding, errors)

kwargs = {}
kwargs["name"] = _ensure_decoded(self.index_name)

if self.freq is not None:
    kwargs["freq"] = _ensure_decoded(self.freq)

factory: type[Index] | type[DatetimeIndex] = Index
if is_datetime64_dtype(values.dtype) or is_datetime64tz_dtype(values.dtype):
    factory = DatetimeIndex
elif values.dtype == "i8" and "freq" in kwargs:
    # PeriodIndex data is stored as i8
    # error: Incompatible types in assignment (expression has type
    # "Callable[[Any, KwArg(Any)], PeriodIndex]", variable has type
    # "Union[Type[Index], Type[DatetimeIndex]]")
    factory = lambda x, **kwds: PeriodIndex(  # type: ignore[assignment]
        ordinal=x, **kwds
    )

# making an Index instance could throw a number of different errors
try:
    new_pd_index = factory(values, **kwargs)
except ValueError:
    # if the output freq is different that what we recorded,
    # it should be None (see also 'doc example part 2')
    if "freq" in kwargs:
        kwargs["freq"] = None
    new_pd_index = factory(values, **kwargs)
final_pd_index = _set_tz(new_pd_index, self.tz)
exit((final_pd_index, final_pd_index))
