# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
# https://github.com/pandas-dev/pandas/pull/28647
monkeypatch.setitem(sys.modules, "pandas_dummy_backend", dummy_backend)
pandas.set_option("plotting.backend", "pandas_dummy_backend")
df = pandas.DataFrame({"A": [1, 2, 3]})
df.plot(kind="not a real kind")
