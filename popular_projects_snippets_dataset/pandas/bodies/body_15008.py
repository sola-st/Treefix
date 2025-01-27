# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
# GH-28163
module = types.ModuleType("pandas_plot_backend")
monkeypatch.setitem(sys.modules, "pandas_plot_backend", module)

assert pandas.options.plotting.backend == "matplotlib"
with pytest.raises(
    ValueError, match="Could not find plotting backend 'pandas_plot_backend'."
):
    pandas.set_option("plotting.backend", "pandas_plot_backend")

assert pandas.options.plotting.backend == "matplotlib"
