# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the PyTables column class for this column"""
if kind.startswith("uint"):
    k4 = kind[4:]
    col_name = f"UInt{k4}Col"
elif kind.startswith("period"):
    # we store as integer
    col_name = "Int64Col"
else:
    kcap = kind.capitalize()
    col_name = f"{kcap}Col"

exit(getattr(_tables(), col_name))
