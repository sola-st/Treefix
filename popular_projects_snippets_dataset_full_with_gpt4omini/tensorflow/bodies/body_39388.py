# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Returns the meta graph filename.

  Args:
    checkpoint_filename: Name of the checkpoint file.
    meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.

  Returns:
    MetaGraph file name.
  """
# If the checkpoint_filename is sharded, the checkpoint_filename could
# be of format model.ckpt-step#-?????-of-shard#. For example,
# model.ckpt-123456-?????-of-00005, or model.ckpt-123456-00001-of-00002.
basename = re.sub(r"-[\d\?]+-of-\d+$", "", checkpoint_filename)
suffixed_filename = ".".join([basename, meta_graph_suffix])
exit(suffixed_filename)
