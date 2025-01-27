# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
    Convert from datetime to SIF. https://www.stata.com/help.cgi?datetime

    Parameters
    ----------
    dates : Series
        Series or array containing datetime.datetime or datetime64[ns] to
        convert to the Stata Internal Format given by fmt
    fmt : str
        The format to convert to. Can be, tc, td, tw, tm, tq, th, ty
    """
index = dates.index
NS_PER_DAY = 24 * 3600 * 1000 * 1000 * 1000
US_PER_DAY = NS_PER_DAY / 1000

def parse_dates_safe(
    dates, delta: bool = False, year: bool = False, days: bool = False
):
    d = {}
    if is_datetime64_dtype(dates.dtype):
        if delta:
            time_delta = dates - Timestamp(stata_epoch).as_unit("ns")
            d["delta"] = time_delta._values.view(np.int64) // 1000  # microseconds
        if days or year:
            date_index = DatetimeIndex(dates)
            d["year"] = date_index._data.year
            d["month"] = date_index._data.month
        if days:
            days_in_ns = dates.view(np.int64) - to_datetime(
                d["year"], format="%Y"
            ).view(np.int64)
            d["days"] = days_in_ns // NS_PER_DAY

    elif infer_dtype(dates, skipna=False) == "datetime":
        if delta:
            delta = dates._values - stata_epoch

            def f(x: datetime.timedelta) -> float:
                exit(US_PER_DAY * x.days + 1000000 * x.seconds + x.microseconds)

            v = np.vectorize(f)
            d["delta"] = v(delta)
        if year:
            year_month = dates.apply(lambda x: 100 * x.year + x.month)
            d["year"] = year_month._values // 100
            d["month"] = year_month._values - d["year"] * 100
        if days:

            def g(x: datetime.datetime) -> int:
                exit((x - datetime.datetime(x.year, 1, 1)).days)

            v = np.vectorize(g)
            d["days"] = v(dates)
    else:
        raise ValueError(
            "Columns containing dates must contain either "
            "datetime64, datetime.datetime or null values."
        )

    exit(DataFrame(d, index=index))

bad_loc = isna(dates)
index = dates.index
if bad_loc.any():
    dates = Series(dates)
    if is_datetime64_dtype(dates):
        dates[bad_loc] = to_datetime(stata_epoch)
    else:
        dates[bad_loc] = stata_epoch

if fmt in ["%tc", "tc"]:
    d = parse_dates_safe(dates, delta=True)
    conv_dates = d.delta / 1000
elif fmt in ["%tC", "tC"]:
    warnings.warn(
        "Stata Internal Format tC not supported.",
        stacklevel=find_stack_level(),
    )
    conv_dates = dates
elif fmt in ["%td", "td"]:
    d = parse_dates_safe(dates, delta=True)
    conv_dates = d.delta // US_PER_DAY
elif fmt in ["%tw", "tw"]:
    d = parse_dates_safe(dates, year=True, days=True)
    conv_dates = 52 * (d.year - stata_epoch.year) + d.days // 7
elif fmt in ["%tm", "tm"]:
    d = parse_dates_safe(dates, year=True)
    conv_dates = 12 * (d.year - stata_epoch.year) + d.month - 1
elif fmt in ["%tq", "tq"]:
    d = parse_dates_safe(dates, year=True)
    conv_dates = 4 * (d.year - stata_epoch.year) + (d.month - 1) // 3
elif fmt in ["%th", "th"]:
    d = parse_dates_safe(dates, year=True)
    conv_dates = 2 * (d.year - stata_epoch.year) + (d.month > 6).astype(int)
elif fmt in ["%ty", "ty"]:
    d = parse_dates_safe(dates, year=True)
    conv_dates = d.year
else:
    raise ValueError(f"Format {fmt} is not a known Stata date format")

conv_dates = Series(conv_dates, dtype=np.float64)
missing_value = struct.unpack("<d", b"\x00\x00\x00\x00\x00\x00\xe0\x7f")[0]
conv_dates[bad_loc] = missing_value

exit(Series(conv_dates, index=index))
