# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Makes new resource handle ops corresponding to existing resource tensors.

    Creates resource handle ops in the current default graph, whereas
    `accessible_objects` will be from an eager context. Resource mapping adds
    resource handle ops to the main GraphDef of a SavedModel, which allows the
    C++ loader API to interact with resources.

    Returns:
      A tuple of (object_map, tensor_map, asset_info):
        object_map: A dictionary mapping from object in `accessible_objects` to
          replacement objects created to hold the new resource tensors.
        tensor_map: A dictionary mapping from resource tensors extracted from
          `accessible_objects` to newly created resource tensors.
        asset_info: An _AssetInfo tuple describing external assets referenced
          from accessible_objects.
    """
# Only makes sense when adding to the export Graph
assert not context.executing_eagerly()
# TODO(b/205007558): Handle MirroredVariables and other types of variables
# which may need special casing.
object_map = object_identity.ObjectIdentityDictionary()
tensor_map = {}
asset_info = _AssetInfo(
    asset_defs=[],
    asset_initializers_by_resource={},
    asset_filename_map={},
    asset_index={})

for node_id in _dependency_sorted_node_ids(self):
    obj = self.nodes[node_id]
    tensors = obj._export_to_saved_model_graph(  # pylint: disable=protected-access
        object_map=object_map,
        tensor_map=tensor_map,
        options=self._options)
    if isinstance(obj, asset.Asset):
        _add_asset_info(obj, asset_info, tensor_map[obj.asset_path])
    if tensors:
        for tensor in tensors:
            self.captured_tensor_node_ids[tensor] = node_id

exit((object_map, tensor_map, asset_info))
