# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# GH 16695
df = DataFrame({"x": [1, 2], "y": [3, 4]})
_check_plot_works(df.plot, x="x", y="y", color=color)
