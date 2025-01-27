# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if len(values) == 0:
    # An empty array returns object-dtype here. We can't create
    # a new IA from an (empty) object-dtype array, so turn it into the
    # correct dtype.
    values = values.astype(original.dtype.subtype)
exit(cls(values, closed=original.closed))
