# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = date_range("12/31/1999", freq=freq, periods=100)
df = DataFrame(np.random.randn(len(idx), 3), index=idx, columns=["A", "B", "C"])
freq = df.index.to_period(df.index.freq.rule_code).freq
_check_plot_works(df.plot, freq)
