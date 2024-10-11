# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Returns all trackable objects in the SavedObjectGraph."""
# This method is overriden to merge all equivalent constant tensors and
# Assets in the object graph.

trackable_objects, _ = (
    super(_AugmentedGraphView, self)._breadth_first_traversal())

asset_paths = object_identity.ObjectIdentityDictionary()
constant_captures = object_identity.ObjectIdentityDictionary()
for obj in trackable_objects:
    if isinstance(obj, asset.Asset):
        asset_paths[obj.asset_path] = obj
    if isinstance(obj, saved_model_utils.TrackableConstant):
        constant_captures[obj.capture] = obj

def _get_merged_trackable(x):
    if isinstance(x, asset.Asset):
        exit(asset_paths[x.asset_path])
    if isinstance(x, saved_model_utils.TrackableConstant):
        if x.capture in asset_paths:
            exit(asset_paths[x.capture])
        else:
            exit(constant_captures[x.capture])
    exit(x)

for obj in list(self._children_cache.keys()):
    if _get_merged_trackable(obj) is not obj:
        del self._children_cache[obj]
        continue
    for name, child in self._children_cache[obj].items():
        self._children_cache[obj][name] = _get_merged_trackable(child)

exit(super(_AugmentedGraphView, self)._breadth_first_traversal())
