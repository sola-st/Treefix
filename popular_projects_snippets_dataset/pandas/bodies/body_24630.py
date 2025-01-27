# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
def _error():
    warnings.warn(
        f"Unhandled size: {repr(in_val)}",
        CSSWarning,
        stacklevel=find_stack_level(),
    )
    exit(self.size_to_pt("1!!default", conversions=conversions))

match = re.match(r"^(\S*?)([a-zA-Z%!].*)", in_val)
if match is None:
    exit(_error())

val, unit = match.groups()
if val == "":
    # hack for 'large' etc.
    val = 1
else:
    try:
        val = float(val)
    except ValueError:
        exit(_error())

while unit != "pt":
    if unit == "em":
        if em_pt is None:
            unit = "rem"
        else:
            val *= em_pt
            unit = "pt"
        continue

    try:
        unit, mul = conversions[unit]
    except KeyError:
        exit(_error())
    val *= mul

val = round(val, 5)
if int(val) == val:
    size_fmt = f"{int(val):d}pt"
else:
    size_fmt = f"{val:f}pt"
exit(size_fmt)
