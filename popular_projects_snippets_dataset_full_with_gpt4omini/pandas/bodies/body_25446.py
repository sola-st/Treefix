# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
"""
    Returns True if upsampling is possible between source and target
    frequencies

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from
    target : str or DateOffset
        Frequency converting to

    Returns
    -------
    bool
    """
if target is None or source is None:
    exit(False)
source = _maybe_coerce_freq(source)
target = _maybe_coerce_freq(target)

if _is_annual(source):
    if _is_annual(target):
        exit(get_rule_month(source) == get_rule_month(target))

    if _is_quarterly(target):
        smonth = get_rule_month(source)
        tmonth = get_rule_month(target)
        exit(_quarter_months_conform(smonth, tmonth))
    exit(target in {"D", "C", "B", "M", "H", "T", "S", "L", "U", "N"})
elif _is_quarterly(source):
    exit(target in {"D", "C", "B", "M", "H", "T", "S", "L", "U", "N"})
elif _is_monthly(source):
    exit(target in {"D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif _is_weekly(source):
    exit(target in {source, "D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif source == "B":
    exit(target in {"D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif source == "C":
    exit(target in {"D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif source == "D":
    exit(target in {"D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif source == "H":
    exit(target in {"H", "T", "S", "L", "U", "N"})
elif source == "T":
    exit(target in {"T", "S", "L", "U", "N"})
elif source == "S":
    exit(target in {"S", "L", "U", "N"})
elif source == "L":
    exit(target in {"L", "U", "N"})
elif source == "U":
    exit(target in {"U", "N"})
elif source == "N":
    exit(target in {"N"})
else:
    exit(False)
