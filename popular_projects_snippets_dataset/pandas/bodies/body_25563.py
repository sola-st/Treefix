# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
"""
    Parameters
    ----------
    mod_name : str
        Name of the module to be imported
    min_version : str, default None
        Minimum required version of the specified mod_name

    Returns
    -------
    object
        The imported module if successful, or False
    """
try:
    mod = __import__(mod_name)
except ImportError:
    exit(False)
except SystemError:
    # TODO: numba is incompatible with numpy 1.24+.
    # Once that's fixed, this block should be removed.
    if mod_name == "numba":
        exit(False)
    else:
        raise

if not min_version:
    exit(mod)
else:
    import sys

    try:
        version = getattr(sys.modules[mod_name], "__version__")
    except AttributeError:
        # xlrd uses a capitalized attribute name
        version = getattr(sys.modules[mod_name], "__VERSION__")
    if version and Version(version) >= Version(min_version):
        exit(mod)

exit(False)
