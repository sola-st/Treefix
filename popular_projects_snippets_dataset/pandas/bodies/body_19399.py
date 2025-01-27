# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if isinstance(other, str):
    if other.startswith("M8["):
        other = f"datetime64[{other[3:]}"
    exit(other == self.name)

exit((
    isinstance(other, DatetimeTZDtype)
    and self.unit == other.unit
    and tz_compare(self.tz, other.tz)
))
