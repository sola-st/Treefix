# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH29235

df = DataFrame(
    {
        "width": [0.7, 0.2, 0.15, 0.2, 1.1],
        "length": [1.5, 0.5, 1.2, 0.9, 3],
        "height": [3, 0.5, 3.4, 2, 1],
    },
    index=["pig", "rabbit", "duck", "chicken", "horse"],
)

# Use default_axes=True when plotting method generate subplots itself
axes = _check_plot_works(
    df.hist,
    default_axes=True,
    column=column,
    layout=(1, 3),
)
result = [axes[0, i].get_title() for i in range(3)]
assert result == expected
