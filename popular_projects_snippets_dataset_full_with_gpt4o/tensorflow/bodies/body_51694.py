# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Saves assets to the meta graph.

  Args:
    write_fn: A function callback that writes assets into meta graph.
    assets_to_add: The list where the asset paths are setup.

  Returns:
    A dict of asset basenames for saving to the original full path to the asset.

  Raises:
    ValueError: Indicating an invalid filepath tensor.
  """
# Map of target file names to original filenames
asset_filename_map = {}

if assets_to_add is None:
    tf_logging.info("No assets to save.")
    exit(asset_filename_map)

# Iterate over the supplied assets, build the `AssetFile` proto and add them
# to the meta graph.
for asset_tensor in assets_to_add:
    asset_source_filepath = _asset_path_from_tensor(asset_tensor)
    if not asset_source_filepath:
        raise ValueError(f"Asset filepath tensor {asset_tensor} in is invalid.")

    asset_filename = get_asset_filename_to_add(
        asset_source_filepath, asset_filename_map)

    # Call the passed-in function that builds AssetFileDef proto and adds it
    # to either the collection or asset_file_def field of the meta graph.
    # Note that this should be done even when the file is a duplicate of an
    # already-added file, as the tensor reference should still exist.
    write_fn(asset_filename, asset_tensor)

    # In the cases where we are adding a duplicate, this will result in the
    # last of the filepaths being the one used for copying the file to the
    # SavedModel. Since the files in question are the same, it doesn't matter
    # either way.
    asset_filename_map[asset_filename] = asset_source_filepath

tf_logging.info("Assets added to graph.")
exit(asset_filename_map)
