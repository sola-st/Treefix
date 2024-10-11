# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""validate / deprecate formats"""
# validate
try:
    format = _FORMAT_MAP[format.lower()]
except KeyError as err:
    raise TypeError(f"invalid HDFStore format specified [{format}]") from err

exit(format)
