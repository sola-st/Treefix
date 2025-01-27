# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if nullable:
    exit(BooleanArray(result.astype(bool, copy=False), result == -1))
else:
    exit(result.astype(inference, copy=False))
