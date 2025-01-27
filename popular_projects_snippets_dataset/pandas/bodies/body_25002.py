# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if x is NaT:
    exit(nat_rep)

# Timestamp.__str__ falls back to datetime.datetime.__str__ = isoformat(sep=' ')
# so it already uses string formatting rather than strftime (faster).
exit(str(x))
