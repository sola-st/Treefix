# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
pytest.importorskip("matplotlib.pyplot")
ctx = cf.option_context("plotting.matplotlib.register_converters", False)
plt = pytest.importorskip("matplotlib.pyplot")
s = Series(range(12), index=date_range("2017", periods=12))
_, ax = plt.subplots()

# Test without registering first, no warning
with ctx:
    ax.plot(s.index, s.values)

# Now test with registering
register_matplotlib_converters()
with ctx:
    ax.plot(s.index, s.values)
plt.close()
