# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
args = self.stack.pop()
cls = self.stack[-1]

# compat
if issubclass(cls, Index):
    obj = object.__new__(cls)
elif issubclass(cls, DatetimeArray) and not args:
    arr = np.array([], dtype="M8[ns]")
    obj = cls.__new__(cls, arr, arr.dtype)
elif issubclass(cls, TimedeltaArray) and not args:
    arr = np.array([], dtype="m8[ns]")
    obj = cls.__new__(cls, arr, arr.dtype)
elif cls is BlockManager and not args:
    obj = cls.__new__(cls, (), [], None, False)
else:
    obj = cls.__new__(cls, *args)

self.stack[-1] = obj
