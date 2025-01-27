# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
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
