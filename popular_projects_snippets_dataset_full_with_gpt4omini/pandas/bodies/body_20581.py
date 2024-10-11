# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py

valid_field_set = {
    "year",
    "month",
    "day",
    "quarter",
    "hour",
    "minute",
    "second",
}

if not set(fields).issubset(valid_field_set):
    argument = list(set(fields) - valid_field_set)[0]
    raise TypeError(f"__new__() got an unexpected keyword argument {argument}")

name = maybe_extract_name(name, data, cls)

if data is None and ordinal is None:
    # range-based.
    if not fields:
        # test_pickle_compat_construction
        cls._raise_scalar_data_error(None)

    data, freq2 = PeriodArray._generate_range(None, None, None, freq, fields)
    # PeriodArray._generate range does validation that fields is
    # empty when really using the range-based constructor.
    freq = freq2

    data = PeriodArray(data, freq=freq)
else:
    freq = validate_dtype_freq(dtype, freq)

    # PeriodIndex allow PeriodIndex(period_index, freq=different)
    # Let's not encourage that kind of behavior in PeriodArray.

    if freq and isinstance(data, cls) and data.freq != freq:
        # TODO: We can do some of these with no-copy / coercion?
        # e.g. D -> 2D seems to be OK
        data = data.asfreq(freq)

    if data is None and ordinal is not None:
        # we strangely ignore `ordinal` if data is passed.
        ordinal = np.asarray(ordinal, dtype=np.int64)
        data = PeriodArray(ordinal, freq=freq)
    else:
        # don't pass copy here, since we copy later.
        data = period_array(data=data, freq=freq)

if copy:
    data = data.copy()

exit(cls._simple_new(data, name=name))
