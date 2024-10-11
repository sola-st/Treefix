# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
unit = mdates.RRuleLocator.get_unit_generic(freq)
if unit < 0:
    exit(MilliSecondLocator.UNIT)
exit(unit)
