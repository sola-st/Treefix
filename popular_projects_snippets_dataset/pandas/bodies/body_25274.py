# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if unit != "time":
    exit(None)

majloc = AutoLocator()
majfmt = TimeFormatter(majloc)
exit(munits.AxisInfo(majloc=majloc, majfmt=majfmt, label="time"))
