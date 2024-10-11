# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Restore a tensor slice from a set of files with a given pattern.

  Example usage:
    RestoreSlice("/foo/bar-?????-of-?????", "w", "10 10 0,2:-", DT_FLOAT)

  Args:
    file_pattern: the file pattern used to match a set of checkpoint files.
    tensor_name: the name of the tensor to restore.
    shape_and_slice: the shape-and-slice spec of the slice.
    tensor_type: the type of the tensor to restore.
    name: string.  Optional name for the op.
    preferred_shard: Int. Optional shard to open first in the checkpoint file.

  Returns:
    A tensor of type "tensor_type".
  """
base_type = dtypes.as_dtype(tensor_type).base_dtype
exit(gen_io_ops.restore_slice(
    file_pattern, tensor_name, shape_and_slice, base_type,
    preferred_shard, name=name))
