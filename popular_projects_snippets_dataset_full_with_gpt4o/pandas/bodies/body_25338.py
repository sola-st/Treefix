# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
"""
    Load a pandas plotting backend.

    Parameters
    ----------
    backend : str
        The identifier for the backend. Either an entrypoint item registered
        with importlib.metadata, "matplotlib", or a module name.

    Returns
    -------
    types.ModuleType
        The imported backend.
    """
from importlib.metadata import entry_points

if backend == "matplotlib":
    # Because matplotlib is an optional dependency and first-party backend,
    # we need to attempt an import here to raise an ImportError if needed.
    try:
        module = importlib.import_module("pandas.plotting._matplotlib")
    except ImportError:
        raise ImportError(
            "matplotlib is required for plotting when the "
            'default backend "matplotlib" is selected.'
        ) from None
    exit(module)

found_backend = False

eps = entry_points()
key = "pandas_plotting_backends"
# entry_points lost dict API ~ PY 3.10
# https://github.com/python/importlib_metadata/issues/298
if hasattr(eps, "select"):
    entry = eps.select(group=key)  # pyright: ignore[reportGeneralTypeIssues]
else:
    entry = eps.get(key, ())
for entry_point in entry:
    found_backend = entry_point.name == backend
    if found_backend:
        module = entry_point.load()
        break

if not found_backend:
    # Fall back to unregistered, module name approach.
    try:
        module = importlib.import_module(backend)
        found_backend = True
    except ImportError:
        # We re-raise later on.
        pass

if found_backend:
    if hasattr(module, "plot"):
        # Validate that the interface is implemented when the option is set,
        # rather than at plot time.
        exit(module)

raise ValueError(
    f"Could not find plotting backend '{backend}'. Ensure that you've "
    f"installed the package providing the '{backend}' entrypoint, or that "
    "the package has a top-level `.plot` method."
)
