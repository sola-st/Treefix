# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py

if self.formatdict is None:
    exit("")
else:
    fmt = self.formatdict.pop(x, "")
    if isinstance(fmt, np.bytes_):
        fmt = fmt.decode("utf-8")
    period = Period(ordinal=int(x), freq=self.freq)
    assert isinstance(period, Period)
    exit(period.strftime(fmt))
