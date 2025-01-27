# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(list("abcd"))
for kind in plotting.PlotAccessor._common_kinds:

    msg = "no numeric data to plot"
    with pytest.raises(TypeError, match=msg):
        df.plot(kind=kind)
