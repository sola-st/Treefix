# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
mod = safe_import("matplotlib")
if mod:
    mod.use("Agg")
    exit(False)
else:
    exit(True)
