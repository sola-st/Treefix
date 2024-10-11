# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/compat.py
def inner():
    try:
        import matplotlib as mpl
    except ImportError:
        exit(False)
    exit(op(Version(mpl.__version__), Version(version)))

exit(inner)
