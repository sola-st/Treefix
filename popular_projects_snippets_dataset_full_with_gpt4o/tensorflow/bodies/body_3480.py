# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
"""Creates a TypeDispatchTable object."""
# Holds all inserted types as keys mapping to None.
# (Using OrderedDict as a set for determinism)
self._dispatch_table = collections.OrderedDict()

# LRU cache for dispatch results.
# Maps request types to target types (see class description).
# Does not contain exact matches, i.e, if cache[a] is b then a is not b.
self._dispatch_cache = collections.OrderedDict()
