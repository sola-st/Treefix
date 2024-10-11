# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
# type: (AttributeSentinel, AttributeSentinel) -> None

# Properly tracking removal is quite challenging; however since this is only
# used to invalidate a cache it's alright to be overly conservative. We need
# to invalidate the cache of `node` (since it has implicitly gained a child)
# but we don't need to invalidate self since attributes should not depend on
# parent Layers.
self._parents.add(node)
node.invalidate_all()
