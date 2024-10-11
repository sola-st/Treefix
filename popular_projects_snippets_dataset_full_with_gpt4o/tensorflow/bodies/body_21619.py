# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""Overrides initialization op of given variable or list of variables.

  Calls `_set_checkpoint_initializer` for each variable in the given list of
  variables.

  Args:
    variable_or_list: `tf.Variable` object or a list of `tf.Variable` objects.
    ckpt_file: string, full path of the checkpoint.
    tensor_name: Name of the tensor to load from the checkpoint.

  Raises:
    ValueError: if all objects in `variable_or_list` are not partitions of the
      same large variable.
  """
if isinstance(variable_or_list, (list, tuple)):
    # A set of slices.
    slice_name = None
    for v in variable_or_list:
        slice_info = v._save_slice_info  # pylint:disable=protected-access
        if slice_name is None:
            slice_name = slice_info.full_name
        elif slice_name != slice_info.full_name:
            raise ValueError("Slices must all be from the same tensor: %s != %s" %
                             (slice_name, slice_info.full_name))
        _set_checkpoint_initializer(v, ckpt_file, tensor_name, slice_info.spec)
else:
    _set_checkpoint_initializer(variable_or_list, ckpt_file, tensor_name, "")
