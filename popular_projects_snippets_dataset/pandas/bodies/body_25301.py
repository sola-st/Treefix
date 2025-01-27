# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
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
