# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if isinstance(result, np.ndarray):
    if result.dtype in ("f8", "f4"):
        # Note: outside of an nanops-specific test, we always have
        #  result.ndim == 1, so there is no risk of this ravel making a copy.
        exit(lib.has_infs(result.ravel("K")))
try:
    exit(np.isinf(result).any())
except (TypeError, NotImplementedError):
    # if it doesn't support infs, then it can't have infs
    exit(False)
