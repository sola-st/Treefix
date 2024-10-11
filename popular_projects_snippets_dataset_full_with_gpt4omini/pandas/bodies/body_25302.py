# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
# error: "BaseOffset" has no attribute "_period_dtype_code"
dtype_code = freq._period_dtype_code  # type: ignore[attr-defined]
freq_group = FreqGroup.from_period_dtype_code(dtype_code)

periodsperday = -1

if dtype_code >= FreqGroup.FR_HR.value:
    if freq_group == FreqGroup.FR_NS:
        periodsperday = 24 * 60 * 60 * 1000000000
    elif freq_group == FreqGroup.FR_US:
        periodsperday = 24 * 60 * 60 * 1000000
    elif freq_group == FreqGroup.FR_MS:
        periodsperday = 24 * 60 * 60 * 1000
    elif freq_group == FreqGroup.FR_SEC:
        periodsperday = 24 * 60 * 60
    elif freq_group == FreqGroup.FR_MIN:
        periodsperday = 24 * 60
    elif freq_group == FreqGroup.FR_HR:
        periodsperday = 24
    else:  # pragma: no cover
        raise ValueError(f"unexpected frequency: {dtype_code}")
    periodsperyear = 365 * periodsperday
    periodspermonth = 28 * periodsperday

elif freq_group == FreqGroup.FR_BUS:
    periodsperyear = 261
    periodspermonth = 19
elif freq_group == FreqGroup.FR_DAY:
    periodsperyear = 365
    periodspermonth = 28
elif freq_group == FreqGroup.FR_WK:
    periodsperyear = 52
    periodspermonth = 3
else:  # pragma: no cover
    raise ValueError("unexpected frequency")

# save this for later usage
vmin_orig = vmin

(vmin, vmax) = (
    Period(ordinal=int(vmin), freq=freq),
    Period(ordinal=int(vmax), freq=freq),
)
assert isinstance(vmin, Period)
assert isinstance(vmax, Period)
span = vmax.ordinal - vmin.ordinal + 1
dates_ = period_range(start=vmin, end=vmax, freq=freq)
# Initialize the output
info = np.zeros(
    span, dtype=[("val", np.int64), ("maj", bool), ("min", bool), ("fmt", "|S20")]
)
info["val"][:] = dates_.asi8
info["fmt"][:] = ""
info["maj"][[0, -1]] = True
# .. and set some shortcuts
info_maj = info["maj"]
info_min = info["min"]
info_fmt = info["fmt"]

def first_label(label_flags):
    if (label_flags[0] == 0) and (label_flags.size > 1) and ((vmin_orig % 1) > 0.0):
        exit(label_flags[1])
    else:
        exit(label_flags[0])

    # Case 1. Less than a month
if span <= periodspermonth:
    day_start = period_break(dates_, "day")
    month_start = period_break(dates_, "month")

    def _hour_finder(label_interval, force_year_start) -> None:
        _hour = dates_.hour
        _prev_hour = (dates_ - 1 * dates_.freq).hour
        hour_start = (_hour - _prev_hour) != 0
        info_maj[day_start] = True
        info_min[hour_start & (_hour % label_interval == 0)] = True
        year_start = period_break(dates_, "year")
        info_fmt[hour_start & (_hour % label_interval == 0)] = "%H:%M"
        info_fmt[day_start] = "%H:%M\n%d-%b"
        info_fmt[year_start] = "%H:%M\n%d-%b\n%Y"
        if force_year_start and not has_level_label(year_start, vmin_orig):
            info_fmt[first_label(day_start)] = "%H:%M\n%d-%b\n%Y"

    def _minute_finder(label_interval) -> None:
        hour_start = period_break(dates_, "hour")
        _minute = dates_.minute
        _prev_minute = (dates_ - 1 * dates_.freq).minute
        minute_start = (_minute - _prev_minute) != 0
        info_maj[hour_start] = True
        info_min[minute_start & (_minute % label_interval == 0)] = True
        year_start = period_break(dates_, "year")
        info_fmt = info["fmt"]
        info_fmt[minute_start & (_minute % label_interval == 0)] = "%H:%M"
        info_fmt[day_start] = "%H:%M\n%d-%b"
        info_fmt[year_start] = "%H:%M\n%d-%b\n%Y"

    def _second_finder(label_interval) -> None:
        minute_start = period_break(dates_, "minute")
        _second = dates_.second
        _prev_second = (dates_ - 1 * dates_.freq).second
        second_start = (_second - _prev_second) != 0
        info["maj"][minute_start] = True
        info["min"][second_start & (_second % label_interval == 0)] = True
        year_start = period_break(dates_, "year")
        info_fmt = info["fmt"]
        info_fmt[second_start & (_second % label_interval == 0)] = "%H:%M:%S"
        info_fmt[day_start] = "%H:%M:%S\n%d-%b"
        info_fmt[year_start] = "%H:%M:%S\n%d-%b\n%Y"

    if span < periodsperday / 12000:
        _second_finder(1)
    elif span < periodsperday / 6000:
        _second_finder(2)
    elif span < periodsperday / 2400:
        _second_finder(5)
    elif span < periodsperday / 1200:
        _second_finder(10)
    elif span < periodsperday / 800:
        _second_finder(15)
    elif span < periodsperday / 400:
        _second_finder(30)
    elif span < periodsperday / 150:
        _minute_finder(1)
    elif span < periodsperday / 70:
        _minute_finder(2)
    elif span < periodsperday / 24:
        _minute_finder(5)
    elif span < periodsperday / 12:
        _minute_finder(15)
    elif span < periodsperday / 6:
        _minute_finder(30)
    elif span < periodsperday / 2.5:
        _hour_finder(1, False)
    elif span < periodsperday / 1.5:
        _hour_finder(2, False)
    elif span < periodsperday * 1.25:
        _hour_finder(3, False)
    elif span < periodsperday * 2.5:
        _hour_finder(6, True)
    elif span < periodsperday * 4:
        _hour_finder(12, True)
    else:
        info_maj[month_start] = True
        info_min[day_start] = True
        year_start = period_break(dates_, "year")
        info_fmt = info["fmt"]
        info_fmt[day_start] = "%d"
        info_fmt[month_start] = "%d\n%b"
        info_fmt[year_start] = "%d\n%b\n%Y"
        if not has_level_label(year_start, vmin_orig):
            if not has_level_label(month_start, vmin_orig):
                info_fmt[first_label(day_start)] = "%d\n%b\n%Y"
            else:
                info_fmt[first_label(month_start)] = "%d\n%b\n%Y"

    # Case 2. Less than three months
elif span <= periodsperyear // 4:
    month_start = period_break(dates_, "month")
    info_maj[month_start] = True
    if dtype_code < FreqGroup.FR_HR.value:
        info["min"] = True
    else:
        day_start = period_break(dates_, "day")
        info["min"][day_start] = True
    week_start = period_break(dates_, "week")
    year_start = period_break(dates_, "year")
    info_fmt[week_start] = "%d"
    info_fmt[month_start] = "\n\n%b"
    info_fmt[year_start] = "\n\n%b\n%Y"
    if not has_level_label(year_start, vmin_orig):
        if not has_level_label(month_start, vmin_orig):
            info_fmt[first_label(week_start)] = "\n\n%b\n%Y"
        else:
            info_fmt[first_label(month_start)] = "\n\n%b\n%Y"
    # Case 3. Less than 14 months ...............
elif span <= 1.15 * periodsperyear:
    year_start = period_break(dates_, "year")
    month_start = period_break(dates_, "month")
    week_start = period_break(dates_, "week")
    info_maj[month_start] = True
    info_min[week_start] = True
    info_min[year_start] = False
    info_min[month_start] = False
    info_fmt[month_start] = "%b"
    info_fmt[year_start] = "%b\n%Y"
    if not has_level_label(year_start, vmin_orig):
        info_fmt[first_label(month_start)] = "%b\n%Y"
    # Case 4. Less than 2.5 years ...............
elif span <= 2.5 * periodsperyear:
    year_start = period_break(dates_, "year")
    quarter_start = period_break(dates_, "quarter")
    month_start = period_break(dates_, "month")
    info_maj[quarter_start] = True
    info_min[month_start] = True
    info_fmt[quarter_start] = "%b"
    info_fmt[year_start] = "%b\n%Y"
# Case 4. Less than 4 years .................
elif span <= 4 * periodsperyear:
    year_start = period_break(dates_, "year")
    month_start = period_break(dates_, "month")
    info_maj[year_start] = True
    info_min[month_start] = True
    info_min[year_start] = False

    month_break = dates_[month_start].month
    jan_or_jul = month_start[(month_break == 1) | (month_break == 7)]
    info_fmt[jan_or_jul] = "%b"
    info_fmt[year_start] = "%b\n%Y"
# Case 5. Less than 11 years ................
elif span <= 11 * periodsperyear:
    year_start = period_break(dates_, "year")
    quarter_start = period_break(dates_, "quarter")
    info_maj[year_start] = True
    info_min[quarter_start] = True
    info_min[year_start] = False
    info_fmt[year_start] = "%Y"
# Case 6. More than 12 years ................
else:
    year_start = period_break(dates_, "year")
    year_break = dates_[year_start].year
    nyears = span / periodsperyear
    (min_anndef, maj_anndef) = _get_default_annual_spacing(nyears)
    major_idx = year_start[(year_break % maj_anndef == 0)]
    info_maj[major_idx] = True
    minor_idx = year_start[(year_break % min_anndef == 0)]
    info_min[minor_idx] = True
    info_fmt[major_idx] = "%Y"

exit(info)
