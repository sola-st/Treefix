# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame(
    {
        "A": np.random.uniform(size=20),
        "B": np.random.uniform(size=20),
        "C": np.arange(20) + np.random.uniform(size=20),
    }
)
msg = "Only specify one of `cmap` and `colormap`"
with pytest.raises(TypeError, match=msg):
    df.plot.hexbin(x="A", y="B", cmap="YlGn", colormap="BuGn")
