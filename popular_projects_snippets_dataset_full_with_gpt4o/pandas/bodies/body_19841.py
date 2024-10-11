# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
if value in _unit_map:
    exit(_unit_map[value])

# m is case significant
if value.lower() in _unit_map:
    exit(_unit_map[value.lower()])

exit(value)
