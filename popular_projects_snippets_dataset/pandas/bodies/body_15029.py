# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 30288
df = DataFrame(
    {
        "length": [1.5, 0.5, 1.2, 0.9, 3],
        "animal": ["pig", "rabbit", "pig", "pig", "rabbit"],
    }
)
# Use default_axes=True when plotting method generate subplots itself
axes = _check_plot_works(
    df.hist,
    default_axes=True,
    column="length",
    by="animal",
    bins=5,
    xrot=0,
)
self._check_ticks_props(axes, xrot=0)
