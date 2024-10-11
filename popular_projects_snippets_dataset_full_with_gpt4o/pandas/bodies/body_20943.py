# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
# GH 3746: Prevent localizing or converting the index by setting tz
raise AttributeError(
    "Cannot directly set timezone. Use tz_localize() "
    "or tz_convert() as appropriate"
)
