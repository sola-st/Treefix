# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
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
