# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
t = datetime(1, 1, 1, 3, 30, 0)
deltas = np.random.randint(1, 20, 3).cumsum()
ts = np.array([(t + timedelta(minutes=int(x))).time() for x in deltas])
df = DataFrame(
    {"a": np.random.randn(len(ts)), "b": np.random.randn(len(ts))}, index=ts
)
fig, ax = self.plt.subplots()
df.plot(ax=ax)

# verify tick labels
ticks = ax.get_xticks()
labels = ax.get_xticklabels()
for _tick, _label in zip(ticks, labels):
    m, s = divmod(int(_tick), 60)
    h, m = divmod(m, 60)
    rs = _label.get_text()
    if len(rs) > 0:
        if s != 0:
            xp = time(h, m, s).strftime("%H:%M:%S")
        else:
            xp = time(h, m, s).strftime("%H:%M")
        assert xp == rs
