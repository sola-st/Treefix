# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"x": [1, 2, 3]})
for kind in plotting.PlotAccessor._common_kinds:

    df.plot(kind=kind)
    getattr(df.plot, kind)()
for kind in ["scatter", "hexbin"]:
    df.plot("x", "x", kind=kind)
    getattr(df.plot, kind)("x", "x")
