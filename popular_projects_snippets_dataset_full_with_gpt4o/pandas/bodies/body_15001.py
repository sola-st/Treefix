# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH 38736
# Ensure string x-axis from the second plot will not be converted to datetime
# due to axis data from first plot
df = DataFrame(
    [1.0],
    index=[Timestamp("2022-02-22 22:22:22")],
)
_check_plot_works(df.plot)
s = Series({"A": 1.0})
_check_plot_works(s.plot.bar)
