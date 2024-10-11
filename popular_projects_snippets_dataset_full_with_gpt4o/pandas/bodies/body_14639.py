# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# 2579 - checking this does not raise
values = [date(1677, 1, 1), date(1677, 1, 2)]
_, ax = self.plt.subplots()
ax.plot(values)

values = [datetime(1677, 1, 1, 12), datetime(1677, 1, 2, 12)]
ax.plot(values)
