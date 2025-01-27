# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Adds edges from an object to its children."""
obj = self._nodes[node_id]
setter = self._node_setters[node_id]

for reference in proto.children:
    setter(obj, reference.local_name, self._nodes[reference.node_id])
    # Note: if an object has an attribute `__call__` add a class method
    # that allows `obj()` syntax to work. This is done per-instance to
    # allow `callable` to be used to find out if an object is callable.
    if reference.local_name == "__call__" and not callable(obj):
        setattr(type(obj), "__call__", _call_attribute)
