# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(100, 4)).cumsum()
_check_plot_works(df.plot, legend=True)
