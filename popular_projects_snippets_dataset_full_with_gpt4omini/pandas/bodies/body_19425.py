# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if isinstance(other, str):
    exit(other.lower() in (self.name.lower(), str(self).lower()))
elif not isinstance(other, IntervalDtype):
    exit(False)
elif self.subtype is None or other.subtype is None:
    # None should match any subtype
    exit(True)
elif self.closed != other.closed:
    exit(False)
else:
    from pandas.core.dtypes.common import is_dtype_equal

    exit(is_dtype_equal(self.subtype, other.subtype))
