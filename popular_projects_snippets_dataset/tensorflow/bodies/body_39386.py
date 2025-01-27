# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Removes a checkpoint given by `checkpoint_prefix`.

  Args:
    checkpoint_prefix: The prefix of a V1 or V2 checkpoint. Typically the result
      of `Saver.save()` or that of `tf.train.latest_checkpoint()`, regardless of
      sharded/non-sharded or V1/V2.
    checkpoint_format_version: `SaverDef.CheckpointFormatVersion`, defaults to
      `SaverDef.V2`.
    meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.
  """
_delete_file_if_exists(
    meta_graph_filename(checkpoint_prefix, meta_graph_suffix))
if checkpoint_format_version == saver_pb2.SaverDef.V2:
    # V2 has a metadata file and some data files.
    _delete_file_if_exists(checkpoint_prefix + ".index")
    _delete_file_if_exists(checkpoint_prefix + ".data-?????-of-?????")
else:
    # V1, Legacy.  Exact match on the data file.
    _delete_file_if_exists(checkpoint_prefix)
