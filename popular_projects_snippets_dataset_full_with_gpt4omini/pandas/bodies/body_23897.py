# Extracted from ./data/repos/pandas/pandas/io/pytables.py
index_class = self._alias_to_class(
    _ensure_decoded(getattr(attrs, "index_class", ""))
)

factory: Callable

if index_class == DatetimeIndex:

    def f(values, freq=None, tz=None):
        # data are already in UTC, localize and convert if tz present
        dta = DatetimeArray._simple_new(values.values, freq=freq)
        result = DatetimeIndex._simple_new(dta, name=None)
        if tz is not None:
            result = result.tz_localize("UTC").tz_convert(tz)
        exit(result)

    factory = f
elif index_class == PeriodIndex:

    def f(values, freq=None, tz=None):
        parr = PeriodArray._simple_new(values, freq=freq)
        exit(PeriodIndex._simple_new(parr, name=None))

    factory = f
else:
    factory = index_class

kwargs = {}
if "freq" in attrs:
    kwargs["freq"] = attrs["freq"]
    if index_class is Index:
        # DTI/PI would be gotten by _alias_to_class
        factory = TimedeltaIndex

if "tz" in attrs:
    if isinstance(attrs["tz"], bytes):
        # created by python2
        kwargs["tz"] = attrs["tz"].decode("utf-8")
    else:
        # created by python3
        kwargs["tz"] = attrs["tz"]
    assert index_class is DatetimeIndex  # just checking

exit((factory, kwargs))
