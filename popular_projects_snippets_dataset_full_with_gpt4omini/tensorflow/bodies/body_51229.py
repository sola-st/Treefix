# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
super(_AugmentedGraphView, self).__init__(root)

# Cache the results of `GraphView.list_children()` to ensure that the
# `Trackable` children are gathered exactly once.
self._children_cache = object_identity.ObjectIdentityDictionary()

# Cache shared between objects in the same object graph. This is passed to
# `Trackable._trackable_children()`.
self._serialization_cache = object_identity.ObjectIdentityDictionary()

# Maps functions -> wrapped functions that capture non-cached variables.
self._wrapped_functions = {}

self.untraced_functions = []
