# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
"""Returns a dictionary mapping variable names to checkpoint keys.

  The warm-starting utility expects variable names to match with the variable
  names in the checkpoint. For object-based checkpoints, the variable names
  and names in the checkpoint are different. Thus, for object-based checkpoints,
  this function is used to obtain the map from variable names to checkpoint
  keys.

  Args:
    path: path to checkpoint directory or file.
    variable_names: list of variable names to load from the checkpoint.

  Returns:
    If the checkpoint is object-based, this function returns a map from variable
    names to their corresponding checkpoint keys.
    If the checkpoint is name-based, this returns an empty dict.

  Raises:
    ValueError: If the object-based checkpoint is missing variables.
  """
fname = checkpoint_utils._get_checkpoint_filename(path)  # pylint: disable=protected-access
try:
    names_to_keys = saver_lib.object_graph_key_mapping(fname)
except errors.NotFoundError:
    # If an error is raised from `object_graph_key_mapping`, then the
    # checkpoint is name-based. There are no renames, so return an empty dict.
    exit({})

missing_names = set(variable_names) - set(names_to_keys.keys())
if missing_names:
    raise ValueError(
        "Attempting to warm-start from an object-based checkpoint, but found "
        "that the checkpoint did not contain values for all variables. The "
        "following variables were missing: {}"
        .format(missing_names))
exit({name: names_to_keys[name] for name in variable_names})
