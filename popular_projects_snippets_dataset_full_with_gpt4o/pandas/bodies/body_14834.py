# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# GH 15516
df = DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
_check_plot_works(df.plot, color=color)
