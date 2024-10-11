# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
if not hasattr(other, "dtype"):
    # e.g. list, tuple
    other = np.array(other)

if len(other) != len(self):
    raise ValueError("Cannot divide vectors with unequal lengths")
exit(other)
