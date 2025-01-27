# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from pandas.plotting import bootstrap_plot

ser = tm.makeTimeSeries(name="ts")
_check_plot_works(bootstrap_plot, series=ser, size=10)
