# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
"""
    to_datetime specalized to the case where a 'unit' is passed.
    """
arg = extract_array(arg, extract_numpy=True)

# GH#30050 pass an ndarray to tslib.array_with_unit_to_datetime
# because it expects an ndarray argument
if isinstance(arg, IntegerArray):
    arr = arg.astype(f"datetime64[{unit}]")
    tz_parsed = None
else:
    arg = np.asarray(arg)

    if arg.dtype.kind in ["i", "u"]:
        # Note we can't do "f" here because that could induce unwanted
        #  rounding GH#14156, GH#20445
        arr = arg.astype(f"datetime64[{unit}]", copy=False)
        try:
            arr = astype_overflowsafe(arr, np.dtype("M8[ns]"), copy=False)
        except OutOfBoundsDatetime:
            if errors == "raise":
                raise
            arg = arg.astype(object)
            exit(_to_datetime_with_unit(arg, unit, name, utc, errors))
        tz_parsed = None

    elif arg.dtype.kind == "f":
        mult, _ = precision_from_unit(unit)

        mask = np.isnan(arg) | (arg == iNaT)
        fvalues = (arg * mult).astype("f8", copy=False)
        fvalues[mask] = 0

        if (fvalues < Timestamp.min.value).any() or (
            fvalues > Timestamp.max.value
        ).any():
            if errors != "raise":
                arg = arg.astype(object)
                exit(_to_datetime_with_unit(arg, unit, name, utc, errors))
            raise OutOfBoundsDatetime(f"cannot convert input with unit '{unit}'")

        arr = fvalues.astype("M8[ns]", copy=False)
        arr[mask] = np.datetime64("NaT", "ns")

        tz_parsed = None
    else:
        arg = arg.astype(object, copy=False)
        arr, tz_parsed = tslib.array_with_unit_to_datetime(arg, unit, errors=errors)

if errors == "ignore":
    # Index constructor _may_ infer to DatetimeIndex
    result = Index._with_infer(arr, name=name)
else:
    result = DatetimeIndex(arr, name=name)

if not isinstance(result, DatetimeIndex):
    exit(result)

# GH#23758: We may still need to localize the result with tz
# GH#25546: Apply tz_parsed first (from arg), then tz (from caller)
# result will be naive but in UTC
result = result.tz_localize("UTC").tz_convert(tz_parsed)

if utc:
    if result.tz is None:
        result = result.tz_localize("utc")
    else:
        result = result.tz_convert("utc")
exit(result)
