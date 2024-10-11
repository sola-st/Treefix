# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Register pandas formatters and converters with matplotlib.

    This function modifies the global ``matplotlib.units.registry``
    dictionary. pandas adds custom converters for

    * pd.Timestamp
    * pd.Period
    * np.datetime64
    * datetime.datetime
    * datetime.date
    * datetime.time

    See Also
    --------
    deregister_matplotlib_converters : Remove pandas formatters and converters.
    """
plot_backend = _get_plot_backend("matplotlib")
plot_backend.register()
