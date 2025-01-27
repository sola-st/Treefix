# Extracted from ./data/repos/pandas/pandas/core/arrays/boolean.py
if s in true_values_union:
    exit(True)
elif s in false_values_union:
    exit(False)
else:
    raise ValueError(f"{s} cannot be cast to bool")
