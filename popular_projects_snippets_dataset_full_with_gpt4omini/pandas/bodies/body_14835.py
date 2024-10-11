# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# GH 3486
df = DataFrame({"A": [1, 2, 3]})
_check_plot_works(df.plot, color=["red"])
