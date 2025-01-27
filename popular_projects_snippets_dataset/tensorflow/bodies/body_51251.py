# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Add `trackable_asset` to `asset_info`."""
original_path_tensor = trackable_asset.asset_path
original_path = tensor_util.constant_value(original_path_tensor)
try:
    original_path = str(original_path.astype(str))
except AttributeError:
    # Already a string rather than a numpy array
    pass

path = builder_impl.get_asset_filename_to_add(
    asset_filepath=original_path,
    asset_filename_map=asset_info.asset_filename_map)
asset_info.asset_filename_map[path] = original_path
asset_def = meta_graph_pb2.AssetFileDef()
asset_def.filename = path
asset_def.tensor_info.name = mapped_path_variable.initial_value.name
asset_info.asset_defs.append(asset_def)
asset_info.asset_initializers_by_resource[original_path_tensor] = (
    mapped_path_variable.initializer)
asset_info.asset_index[trackable_asset] = len(asset_info.asset_defs) - 1
