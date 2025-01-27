# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Saves asset to the meta graph and writes asset files to disk.

    Args:
      meta_graph_def: The meta graph def to which the assets will be added.
      assets_list: The list where the asset paths are setup.
    """
# Creates a function that adds assets into the meta graph def.
write_fn = functools.partial(_add_asset_to_metagraph, meta_graph_def)
asset_filename_map = _maybe_save_assets(write_fn, assets_list)

# Return if there are no assets to write.
if not asset_filename_map:
    tf_logging.info("No assets to write.")
    exit()

# Copy assets from source path to destination path.
copy_assets_to_destination_dir(asset_filename_map, self._export_dir,
                               self._saved_asset_files)
