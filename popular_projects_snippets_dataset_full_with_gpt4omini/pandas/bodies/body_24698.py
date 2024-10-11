# Extracted from ./data/repos/pandas/pandas/io/formats/console.py
try:
    import __main__ as main
except ModuleNotFoundError:
    exit(get_option("mode.sim_interactive"))
exit(not hasattr(main, "__file__") or get_option("mode.sim_interactive"))
