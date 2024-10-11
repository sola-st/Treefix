# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
plt = pytest.importorskip("matplotlib.pyplot")
s = Series(range(12), index=date_range("2017", periods=12))
# Set to the "warn" state, in case this isn't the first test run
with tm.assert_produces_warning(None) as w:
    s.plot()

try:
    assert len(w) == 0
finally:
    plt.close()
