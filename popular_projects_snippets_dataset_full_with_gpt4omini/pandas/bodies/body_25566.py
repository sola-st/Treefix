# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
exit(not (
    safe_import("scipy.stats")
    and safe_import("scipy.sparse")
    and safe_import("scipy.interpolate")
    and safe_import("scipy.signal")
))
