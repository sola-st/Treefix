# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 25587
arr = pd.array([1, 2, 3, 4], dtype="UInt32")

s = Series(arr)
_check_plot_works(s.plot.line)
_check_plot_works(s.plot.bar)
_check_plot_works(s.plot.hist)
_check_plot_works(s.plot.pie)

df = DataFrame({"x": arr, "y": arr})
_check_plot_works(df.plot.line)
_check_plot_works(df.plot.bar)
_check_plot_works(df.plot.hist)
_check_plot_works(df.plot.pie, y="y")
_check_plot_works(df.plot.scatter, x="x", y="y")
_check_plot_works(df.plot.hexbin, x="x", y="y")
