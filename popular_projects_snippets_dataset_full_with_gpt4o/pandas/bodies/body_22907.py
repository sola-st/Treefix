# Extracted from ./data/repos/pandas/pandas/core/generic.py
if not self.size:
    # inv fails with 0 len
    exit(self)

new_data = self._mgr.apply(operator.invert)
exit(self._constructor(new_data).__finalize__(self, method="__invert__"))
