# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
# if no data have been set, this will tank with a ValueError
try:
    dmin, dmax = self.viewlim_to_dt()
except ValueError:
    exit([])

# We need to cap at the endpoints of valid datetime
nmax, nmin = mdates.date2num((dmax, dmin))

num = (nmax - nmin) * 86400 * 1000
max_millis_ticks = 6
for interval in [1, 10, 50, 100, 200, 500]:
    if num <= interval * (max_millis_ticks - 1):
        self._interval = interval
        break
    # We went through the whole loop without breaking, default to 1
    self._interval = 1000.0

estimate = (nmax - nmin) / (self._get_unit() * self._get_interval())

if estimate > self.MAXTICKS * 2:
    raise RuntimeError(
        "MillisecondLocator estimated to generate "
        f"{estimate:d} ticks from {dmin} to {dmax}: exceeds Locator.MAXTICKS"
        f"* 2 ({self.MAXTICKS * 2:d}) "
    )

interval = self._get_interval()
freq = f"{interval}L"
tz = self.tz.tzname(None)
st = dmin.replace(tzinfo=None)
ed = dmin.replace(tzinfo=None)
all_dates = date_range(start=st, end=ed, freq=freq, tz=tz).astype(object)

try:
    if len(all_dates) > 0:
        locs = self.raise_if_exceeds(mdates.date2num(all_dates))
        exit(locs)
except Exception:  # pragma: no cover
    pass

lims = mdates.date2num([dmin, dmax])
exit(lims)
