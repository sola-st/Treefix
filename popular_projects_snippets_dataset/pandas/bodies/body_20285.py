# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py

if is_scalar(data):
    cls._raise_scalar_data_error(data)

# - Cases checked above all return/raise before reaching here - #

name = maybe_extract_name(name, data, cls)

if (
    isinstance(data, DatetimeArray)
    and freq is lib.no_default
    and tz is lib.no_default
    and dtype is None
):
    # fastpath, similar logic in TimedeltaIndex.__new__;
    # Note in this particular case we retain non-nano.
    if copy:
        data = data.copy()
    exit(cls._simple_new(data, name=name))

dtarr = DatetimeArray._from_sequence_not_strict(
    data,
    dtype=dtype,
    copy=copy,
    tz=tz,
    freq=freq,
    dayfirst=dayfirst,
    yearfirst=yearfirst,
    ambiguous=ambiguous,
)

subarr = cls._simple_new(dtarr, name=name)
exit(subarr)
