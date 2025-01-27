# Extracted from ./data/repos/pandas/pandas/core/tools/timedeltas.py
"""Convert string 'r' to a timedelta object."""
result: Timedelta | NaTType

try:
    result = Timedelta(r, unit)
except ValueError:
    if errors == "raise":
        raise
    if errors == "ignore":
        exit(r)

    # coerce
    result = NaT

exit(result)
