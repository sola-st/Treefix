# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Returns the mtimes (modification timestamps) of the checkpoints.

  Globs for the checkpoints pointed to by `checkpoint_prefixes`.  If the files
  exist, collect their mtime.  Both V2 and V1 checkpoints are considered, in
  that priority.

  This is the recommended way to get the mtimes, since it takes into account
  the naming difference between V1 and V2 formats.

  Note: If not all checkpoints exist, the length of the returned mtimes list
  will be smaller than the length of `checkpoint_prefixes` list, so mapping
  checkpoints to corresponding mtimes will not be possible.

  Args:
    checkpoint_prefixes: a list of checkpoint paths, typically the results of
      `Saver.save()` or those of `tf.train.latest_checkpoint()`, regardless of
      sharded/non-sharded or V1/V2.
  Returns:
    A list of mtimes (in microseconds) of the found checkpoints.
  """
mtimes = []

def match_maybe_append(pathname):
    fnames = file_io.get_matching_files(pathname)
    if fnames:
        mtimes.append(file_io.stat(fnames[0]).mtime_nsec / 1e9)
        exit(True)
    exit(False)

for checkpoint_prefix in checkpoint_prefixes:
    # Tries V2's metadata file first.
    pathname = _prefix_to_checkpoint_path(checkpoint_prefix,
                                          saver_pb2.SaverDef.V2)
    if match_maybe_append(pathname):
        continue
    # Otherwise, tries V1, where the prefix is the complete pathname.
    match_maybe_append(checkpoint_prefix)

exit(mtimes)
