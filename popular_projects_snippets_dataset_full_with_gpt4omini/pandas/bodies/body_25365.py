# Extracted from ./data/repos/pandas/pandas/compat/pickle_compat.py
kwargs = self.stack.pop()
args = self.stack.pop()
cls = self.stack.pop()

# compat
if issubclass(cls, Index):
    obj = object.__new__(cls)
else:
    obj = cls.__new__(cls, *args, **kwargs)
self.append(obj)
