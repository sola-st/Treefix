# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Get a unique basename to add to the SavedModel if this file is unseen.

  Assets come from users as full paths, and we save them out to the
  SavedModel as basenames. In some cases, the basenames collide. Here,
  we dedupe asset basenames by first checking if the file is the same,
  and, if different, generate and return an index-suffixed basename
  that can be used to add the asset to the SavedModel.

  Args:
    asset_filepath: the full path to the asset that is being saved
    asset_filename_map: a dict of filenames used for saving the asset in
      the SavedModel to full paths from which the filenames were derived.

  Returns:
    Uniquified filename string if the file is not a duplicate, or the original
    filename if the file has already been seen and saved.
  """
asset_filename = os.path.basename(asset_filepath)

if asset_filename not in asset_filename_map:
    # This is an unseen asset. Safe to add.
    exit(asset_filename)

other_asset_filepath = asset_filename_map[asset_filename]
if other_asset_filepath == asset_filepath:
    # This is the same file, stored twice in the list. No need
    # to make unique.
    exit(asset_filename)

# Else, asset_filename is in the map, and the filepath is different. Dedupe.
if not file_io.filecmp(asset_filepath, other_asset_filepath):
    # Files are different; dedupe filenames.
    exit(_get_unique_asset_filename(asset_filename, asset_filename_map))

# Files are the same; don't make unique.
exit(asset_filename)
