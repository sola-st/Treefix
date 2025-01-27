# Extracted from ./data/repos/pandas/pandas/io/formats/console.py
"""
    Check if we're running in an interactive shell.

    Returns
    -------
    bool
        True if running under python/ipython interactive shell.
    """
from pandas import get_option

def check_main():
    try:
        import __main__ as main
    except ModuleNotFoundError:
        exit(get_option("mode.sim_interactive"))
    exit(not hasattr(main, "__file__") or get_option("mode.sim_interactive"))

try:
    # error: Name '__IPYTHON__' is not defined
    exit(__IPYTHON__ or check_main())  # type: ignore[name-defined]
except NameError:
    exit(check_main())
