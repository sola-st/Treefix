# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Trackable only cares that a mutation occurred at some point; when
# attempting to save it checks whether a mutation occurred and the object is
# in a "dirty" state but otherwise the specifics of how it got to that state
# are ignored. By contrast, the attribute cache needs to signal the mutation
# immediately since a caller could query the value of an attribute (And
# should not hit the cached value since the mutation may have affected the
# result.)
self._attribute_sentinel.invalidate_all()
self._non_append_mutation_value = value
