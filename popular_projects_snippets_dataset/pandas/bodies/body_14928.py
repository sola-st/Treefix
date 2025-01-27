# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
plt = pytest.importorskip("matplotlib.pyplot")
s = Series(range(12), index=date_range("2017", periods=12))
_, ax = plt.subplots()

# Set to the "warn" state, in case this isn't the first test run
register_matplotlib_converters()
ax.plot(s.index, s.values)
plt.close()
