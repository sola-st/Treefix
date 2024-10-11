# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
df = DataFrame(np.random.randn(5, 3), columns=["a", "b", "c"])
axes = df.plot(kind="bar", secondary_y=["a", "c"], subplots=True)
assert axes[0].get_yaxis().get_ticks_position() == "right"
assert axes[1].get_yaxis().get_ticks_position() == "left"
assert axes[2].get_yaxis().get_ticks_position() == "right"
