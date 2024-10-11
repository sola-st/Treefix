# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Saves asset to the meta graph and writes asset files to disk.

    Args:
      assets_collection_to_add: The collection where the asset paths are setup.
    """
# Add assets to the collection with key `saved_model.ASSETS_KEY`, in the
# graph.
asset_filename_map = _maybe_save_assets(_add_asset_to_collection,
                                        assets_collection_to_add)

# Return if there are no assets to write.
if not asset_filename_map:
    tf_logging.info("No assets to write.")
    exit()

# Copy assets from source path to destination path.
copy_assets_to_destination_dir(asset_filename_map, self._export_dir,
                               self._saved_asset_files)
