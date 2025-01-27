# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
monkeypatch.setitem(sys.modules, "pandas_dummy_backend", dummy_backend)

pandas.set_option("plotting.backend", "pandas_dummy_backend")
assert pandas.get_option("plotting.backend") == "pandas_dummy_backend"
assert (
    pandas.plotting._core._get_plot_backend("pandas_dummy_backend") is dummy_backend
)
