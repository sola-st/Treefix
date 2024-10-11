# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
self._parents = weakref.WeakSet()
self.attributes = collections.defaultdict(MutationSentinel)

# The trackable data structure containers are simple pass throughs. They
# don't know or care about particular attributes. As a result, they will
# consider themselves to be in a cached state, so it's up to the Layer
# which contains them to terminate propagation.
self.always_propagate = always_propagate
