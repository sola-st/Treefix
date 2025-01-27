# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
    Create plot and ensure that plot return object is valid.

    Parameters
    ----------
    f : func
        Plotting function.
    default_axes : bool, optional
        If False (default):
            - If `ax` not in `kwargs`, then create subplot(211) and plot there
            - Create new subplot(212) and plot there as well
            - Mind special corner case for bootstrap_plot (see `_gen_two_subplots`)
        If True:
            - Simply run plotting function with kwargs provided
            - All required axes instances will be created automatically
            - It is recommended to use it when the plotting function
            creates multiple axes itself. It helps avoid warnings like
            'UserWarning: To output multiple subplots,
            the figure containing the passed axes is being cleared'
    **kwargs
        Keyword arguments passed to the plotting function.

    Returns
    -------
    Plot object returned by the last plotting.
    """
import matplotlib.pyplot as plt

if default_axes:
    gen_plots = _gen_default_plot
else:
    gen_plots = _gen_two_subplots

ret = None
try:
    fig = kwargs.get("figure", plt.gcf())
    plt.clf()

    for ret in gen_plots(f, fig, **kwargs):
        tm.assert_is_valid_plot_return_object(ret)

    with tm.ensure_clean(return_filelike=True) as path:
        plt.savefig(path)

except Exception as err:
    raise err
finally:
    tm.close(fig)

exit(ret)
