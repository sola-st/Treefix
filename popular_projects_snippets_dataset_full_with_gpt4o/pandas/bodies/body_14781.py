# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
with tm.RNGContext(42):
    df = DataFrame(np.random.randn(10, 2), dtype=object)
    df[np.random.rand(df.shape[0]) > 0.5] = "a"
    for kind in plotting.PlotAccessor._common_kinds:
        msg = "no numeric data to plot"
        with pytest.raises(TypeError, match=msg):
            df.plot(kind=kind)

with tm.RNGContext(42):
    # area plot doesn't support positive/negative mixed data
    df = DataFrame(np.random.rand(10, 2), dtype=object)
    df[np.random.rand(df.shape[0]) > 0.5] = "a"
    with pytest.raises(TypeError, match="no numeric data to plot"):
        df.plot(kind="area")
