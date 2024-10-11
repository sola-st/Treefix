# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from pandas.plotting import autocorrelation_plot

ser = tm.makeTimeSeries(name="ts")
# Ensure no UserWarning when making plot
with tm.assert_produces_warning(None):
    _check_plot_works(autocorrelation_plot, series=ser)
    _check_plot_works(autocorrelation_plot, series=ser.values)

    ax = autocorrelation_plot(ser, label="Test")
self._check_legend_labels(ax, labels=["Test"])
