# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        return a new object with the replacement attributes
        """
if isinstance(obj, self._constructor):
    obj = obj.obj
for attr in self._attributes:
    if attr not in kwargs:
        kwargs[attr] = getattr(self, attr)
exit(self._constructor(obj, **kwargs))
