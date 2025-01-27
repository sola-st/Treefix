# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
monkeypatch.setitem(sys.modules, "pandas_dummy_backend", dummy_backend)
df = pandas.DataFrame([1, 2, 3])

assert pandas.get_option("plotting.backend") == "matplotlib"
assert df.plot(backend="pandas_dummy_backend") == "used_dummy"
