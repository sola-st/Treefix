# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# test period index line plot for DataFrames with multiples (`mlt`)
# of the frequency (`frqncy`) rule code. tests resolution of issue
# #14763
idx = period_range("12/31/1999", freq=frqncy, periods=100)
df = DataFrame(np.random.randn(len(idx), 3), index=idx, columns=["A", "B", "C"])
freq = df.index.asfreq(df.index.freq.rule_code).freq
_check_plot_works(df.plot, freq)
