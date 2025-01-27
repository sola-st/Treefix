# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from pandas.plotting import lag_plot

ser = tm.makeTimeSeries(name="ts")
_check_plot_works(lag_plot, series=ser, **kwargs)
