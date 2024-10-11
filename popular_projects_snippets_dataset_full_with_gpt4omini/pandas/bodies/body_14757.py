# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 18755
df = DataFrame({"a": ["A", "B", "C"], "b": [2, 3, 4]})

_check_plot_works(df.plot.scatter, x="a", y="b")
_check_plot_works(df.plot.scatter, x=0, y=1)

df = DataFrame({"a": ["A", "B", "C"], "b": ["a", "b", "c"]})

_check_plot_works(df.plot.scatter, x="a", y="b")
_check_plot_works(df.plot.scatter, x=0, y=1)
