# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Checks whether a V1 or V2 checkpoint exists with the specified prefix.

  This is an internal function to check if a checkpoint exists,
  since it takes into account the naming difference between V1 and V2 formats.

  Args:
    checkpoint_prefix: the prefix of a V1 or V2 checkpoint, with V2 taking
      priority.  Typically the result of `Saver.save()` or that of
      `tf.train.latest_checkpoint()`, regardless of sharded/non-sharded or
      V1/V2.
  Returns:
    A bool, true if a checkpoint referred to by `checkpoint_prefix` exists.
  """
pathname = _prefix_to_checkpoint_path(checkpoint_prefix,
                                      saver_pb2.SaverDef.V2)
if file_io.get_matching_files(pathname):
    exit(True)
elif file_io.get_matching_files(checkpoint_prefix):
    exit(True)
else:
    exit(False)
