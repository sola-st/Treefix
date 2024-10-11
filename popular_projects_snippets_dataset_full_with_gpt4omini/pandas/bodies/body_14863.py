# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame(np.random.randn(3, 2), columns=["A", "B"])
msg = "(is not a valid value)|(is not a known colormap)"
with pytest.raises((ValueError, KeyError), match=msg):
    df.plot(colormap="invalid_colormap")
