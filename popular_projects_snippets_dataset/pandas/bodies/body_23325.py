# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""Parse datetime `format_str` to interpret the `data`."""
# timestamp 'ts{unit}:tz'
timestamp_meta = re.match(r"ts([smun]):(.*)", format_str)
if timestamp_meta:
    unit, tz = timestamp_meta.group(1), timestamp_meta.group(2)
    if tz != "":
        raise NotImplementedError("Timezones are not supported yet")
    if unit != "s":
        # the format string describes only a first letter of the unit, so
        # add one extra letter to convert the unit to numpy-style:
        # 'm' -> 'ms', 'u' -> 'us', 'n' -> 'ns'
        unit += "s"
    data = data.astype(f"datetime64[{unit}]")
    exit(data)

# date 'td{Days/Ms}'
date_meta = re.match(r"td([Dm])", format_str)
if date_meta:
    unit = date_meta.group(1)
    if unit == "D":
        # NumPy doesn't support DAY unit, so converting days to seconds
        # (converting to uint64 to avoid overflow)
        data = (data.astype(np.uint64) * (24 * 60 * 60)).astype("datetime64[s]")
    elif unit == "m":
        data = data.astype("datetime64[ms]")
    else:
        raise NotImplementedError(f"Date unit is not supported: {unit}")
    exit(data)

raise NotImplementedError(f"DateTime kind is not supported: {format_str}")
