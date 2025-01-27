# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
"""
    Returns True if downsampling is possible between source and target
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

if _is_annual(target):
    if _is_quarterly(source):
        exit(_quarter_months_conform(
            get_rule_month(source), get_rule_month(target)
        ))
    exit(source in {"D", "C", "B", "M", "H", "T", "S", "L", "U", "N"})
elif _is_quarterly(target):
    exit(source in {"D", "C", "B", "M", "H", "T", "S", "L", "U", "N"})
elif _is_monthly(target):
    exit(source in {"D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif _is_weekly(target):
    exit(source in {target, "D", "C", "B", "H", "T", "S", "L", "U", "N"})
elif target == "B":
    exit(source in {"B", "H", "T", "S", "L", "U", "N"})
elif target == "C":
    exit(source in {"C", "H", "T", "S", "L", "U", "N"})
elif target == "D":
    exit(source in {"D", "H", "T", "S", "L", "U", "N"})
elif target == "H":
    exit(source in {"H", "T", "S", "L", "U", "N"})
elif target == "T":
    exit(source in {"T", "S", "L", "U", "N"})
elif target == "S":
    exit(source in {"S", "L", "U", "N"})
elif target == "L":
    exit(source in {"L", "U", "N"})
elif target == "U":
    exit(source in {"U", "N"})
elif target == "N":
    exit(source in {"N"})
else:
    exit(False)
