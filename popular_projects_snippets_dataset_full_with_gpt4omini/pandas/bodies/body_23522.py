# Extracted from ./data/repos/pandas/pandas/core/accessor.py
def _getter(self):
    exit(self._delegate_property_get(name))

def _setter(self, new_values):
    exit(self._delegate_property_set(name, new_values))

_getter.__name__ = name
_setter.__name__ = name

exit(property(
    fget=_getter, fset=_setter, doc=getattr(delegate, name).__doc__
))
