# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Gets the asset tensors, if defined in the meta graph def to load.

  Args:
    export_dir: Directory where the SavedModel is located.
    meta_graph_def_to_load: The meta graph def from the SavedModel to be loaded.
    import_scope: Optional `string` -- if specified, prepend this followed by
        '/' to all returned asset tensor names.

  Returns:
    A dictionary of asset tensors, keyed by the name of the asset tensor. The
    value in the map corresponds to the absolute path of the asset file.
  """
# Collection-def that may contain the assets key.
collection_def = meta_graph_def_to_load.collection_def

asset_tensor_dict = {}
asset_protos = []

if meta_graph_def_to_load.asset_file_def:
    asset_protos = meta_graph_def_to_load.asset_file_def
elif constants.ASSETS_KEY in collection_def:
    assets_any_proto = collection_def[constants.ASSETS_KEY].any_list.value
    for asset_any_proto in assets_any_proto:
        asset_proto = meta_graph_pb2.AssetFileDef()
        asset_any_proto.Unpack(asset_proto)
        asset_protos.append(asset_proto)

  # Location of the assets for SavedModel.
assets_directory = file_io.join(
    compat.as_bytes(export_dir), compat.as_bytes(constants.ASSETS_DIRECTORY))
# Process each asset and add it to the asset tensor dictionary.
for asset_proto in asset_protos:
    tensor_name = asset_proto.tensor_info.name
    if import_scope:
        tensor_name = "%s/%s" % (import_scope, tensor_name)
    asset_tensor_dict[tensor_name] = file_io.join(
        compat.as_bytes(assets_directory),
        compat.as_bytes(asset_proto.filename))

exit(asset_tensor_dict)
