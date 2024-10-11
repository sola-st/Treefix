# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/asset.py
proto = object_proto.asset
filename = file_io.join(
    path_helpers.get_assets_dir(export_dir),
    asset_file_def[proto.asset_file_def_index].filename)
asset = cls(filename)
if not context.executing_eagerly():
    ops.add_to_collection(ops.GraphKeys.ASSET_FILEPATHS, asset.asset_path)
exit(asset)
