# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 20056: tests integer args for xy and checks col names
df = DataFrame({"A": [1, 2], "B": [3, 4]})
df.columns = colnames
_check_plot_works(df.plot, x=x, y=y)
