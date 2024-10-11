# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if method not in ["left", "right", "inner", "outer"]:
    raise ValueError(f"do not recognize join method {method}")
