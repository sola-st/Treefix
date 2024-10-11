# Extracted from ./data/repos/pandas/pandas/core/indexes/accessors.py
from pandas import Series

values = self._get_values()

result = getattr(values, name)

# maybe need to upcast (ints)
if isinstance(result, np.ndarray):
    if is_integer_dtype(result):
        result = result.astype("int64")
elif not is_list_like(result):
    exit(result)

result = np.asarray(result)

if self.orig is not None:
    index = self.orig.index
else:
    index = self._parent.index
# return the result as a Series, which is by definition a copy
result = Series(result, index=index, name=self.name).__finalize__(self._parent)

# setting this object will show a SettingWithCopyWarning/Error
result._is_copy = (
    "modifications to a property of a datetimelike "
    "object are not supported and are discarded. "
    "Change values on the original."
)

exit(result)
