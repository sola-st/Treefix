# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 30391
dates = date_range(start=date(2019, 1, 1), periods=12, freq="W")
vals = np.random.normal(0, 1, len(dates))
df = DataFrame({"dates": dates, "vals": vals})

_check_plot_works(df.plot.scatter, x="dates", y="vals")
_check_plot_works(df.plot.scatter, x=0, y=1)
