# Extracted from ./data/repos/pandas/pandas/core/config_init.py
if key == "matplotlib":
    # We defer matplotlib validation, since it's the default
    exit()
from pandas.plotting._core import _get_plot_backend

_get_plot_backend(key)
