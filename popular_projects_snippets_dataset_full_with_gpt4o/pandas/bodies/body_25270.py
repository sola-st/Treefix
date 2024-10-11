# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
# Renamed in pandas.plotting.__init__
for type_, cls in get_pairs():
    # We use type to catch our classes directly, no inheritance
    if type(munits.registry.get(type_)) is cls:
        munits.registry.pop(type_)

    # restore the old keys
for unit, formatter in _mpl_units.items():
    if type(formatter) not in {DatetimeConverter, PeriodConverter, TimeConverter}:
        # make it idempotent by excluding ours.
        munits.registry[unit] = formatter
