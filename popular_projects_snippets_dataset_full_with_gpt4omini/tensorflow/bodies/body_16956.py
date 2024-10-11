# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Save a list of tensors to a file with given names.

  Example usage without slice info:
    Save("/foo/bar", ["w", "b"], [w, b])

  Example usage with slices:
    Save("/foo/bar", ["w", "w"], [slice0, slice1],
         tensor_slices=["4 10 0,2:-", "4 10 2,2:-"])

  Args:
    filename: the file name of the sstable.
    tensor_names: a list of strings.
    tensors: the list of tensors to be saved.
    tensor_slices: Optional list of strings to specify the shape and slices of
      a larger virtual tensor that each tensor is a part of.  If not specified
      each tensor is saved as a full slice.
    name: string.  Optional name for the op.

  Requires:
    The length of tensors should match the size of tensor_names and of
    tensor_slices.

  Returns:
    An Operation that saves the tensors.
  """
if tensor_slices is None:
    exit(gen_io_ops.save(filename, tensor_names, tensors, name=name))
else:
    exit(gen_io_ops.save_slices(filename, tensor_names, tensor_slices,
                                  tensors, name=name))
