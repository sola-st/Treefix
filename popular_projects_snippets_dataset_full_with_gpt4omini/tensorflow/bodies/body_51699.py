# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Copy all assets from source path to destination path.

  Args:
    asset_filename_map: a dict of filenames used for saving the asset in
      the SavedModel to full paths from which the filenames were derived.
    destination_dir: the destination directory that assets are stored in.
    saved_files: a set of destination filepaths that have already been copied
      and will be skipped
  """
if saved_files is None:
    saved_files = set()

assets_destination_dir = path_helpers.get_or_create_assets_dir(
    destination_dir)

# Copy each asset from source path to destination path.
for asset_basename, asset_source_filepath in asset_filename_map.items():
    asset_destination_filepath = file_io.join(
        compat.as_bytes(assets_destination_dir),
        compat.as_bytes(asset_basename))

    # Copy if source file exists, src & dst are not the same, and dst is not in
    # saved_files
    if (file_io.file_exists(asset_source_filepath) and
        asset_source_filepath != asset_destination_filepath and
        asset_destination_filepath not in saved_files):
        file_io.copy(
            asset_source_filepath, asset_destination_filepath, overwrite=True)
        saved_files.add(asset_destination_filepath)

tf_logging.info("Assets written to: %s",
                compat.as_text(assets_destination_dir))
