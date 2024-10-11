# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
pairs = get_pairs()
for type_, cls in pairs:
    # Cache previous converter if present
    if type_ in munits.registry and not isinstance(munits.registry[type_], cls):
        previous = munits.registry[type_]
        _mpl_units[type_] = previous
    # Replace with pandas converter
    munits.registry[type_] = cls()
