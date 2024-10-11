# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(["a", "b", "c"])
with pytest.raises(TypeError, match="no numeric data to plot"):
    df.plot()
