# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame(np.random.randn(10, 2))
with pytest.raises(ValueError, match="Invalid color argument:"):
    df.plot(color="")
