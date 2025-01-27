# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
msg = (
    'matplotlib is required for plotting when the default backend "matplotlib" is '
    "selected."
)
with pytest.raises(ImportError, match=msg):
    pandas.plotting._core._get_plot_backend("matplotlib")
