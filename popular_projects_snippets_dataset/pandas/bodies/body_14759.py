# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# after fixing GH 18755, should be able to plot categorical data
df = DataFrame({"x": [1, 2, 3, 4], "y": pd.Categorical(["a", "b", "a", "c"])})

_check_plot_works(df.plot.scatter, x=x, y=y)
