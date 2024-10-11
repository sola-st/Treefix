# Extracted from ./data/repos/pandas/pandas/core/frame.py
if x.empty:
    exit(lib.map_infer(x, func, ignore_na=ignore_na))
exit(lib.map_infer(x.astype(object)._values, func, ignore_na=ignore_na))
