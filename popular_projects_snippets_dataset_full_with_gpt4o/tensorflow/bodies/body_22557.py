# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util.py
"""Collects and groups (possibly partitioned) variables into a dictionary.

  The variables can be provided explicitly through vars_to_warm_start, or they
  are retrieved from collections (see below).

  Args:
    vars_to_warm_start: One of the following:

      - A regular expression (string) that captures which variables to
        warm-start (see tf.compat.v1.get_collection).  This expression will
        only consider variables in the TRAINABLE_VARIABLES collection.
      - A list of strings, each representing a full variable name to warm-start.
        These will consider variables in GLOBAL_VARIABLES collection.
      - A list of Variables to warm-start.
      - `None`, in which case all variables in TRAINABLE_VARIABLES will be used.
  Returns:
    A dictionary mapping variable names (strings) to lists of Variables.
  Raises:
    ValueError: If vars_to_warm_start is not a string, `None`, a list of
      `Variables`, or a list of strings.
  """
# TODO(b/143899805): Remove unicode checks when deprecating Python2.
if isinstance(vars_to_warm_start, str) or vars_to_warm_start is None:
    # Both vars_to_warm_start = '.*' and vars_to_warm_start = None will match
    # everything (in TRAINABLE_VARIABLES) here.
    logging.info("Warm-starting variables only in TRAINABLE_VARIABLES.")
    list_of_vars = ops.get_collection(
        ops.GraphKeys.TRAINABLE_VARIABLES, scope=vars_to_warm_start)
elif isinstance(vars_to_warm_start, list):
    if all(isinstance(v, str) for v in vars_to_warm_start):
        list_of_vars = []
        for v in vars_to_warm_start:
            list_of_vars += ops.get_collection(
                ops.GraphKeys.GLOBAL_VARIABLES, scope=v)
    elif all(checkpoint_utils._is_variable(v) for v in vars_to_warm_start):  # pylint: disable=protected-access
        list_of_vars = vars_to_warm_start
    else:
        raise ValueError("If `vars_to_warm_start` is a list, it must be all "
                         "`Variable` or all `str`.  Given types are {}".format(
                             [type(v) for v in vars_to_warm_start]))
else:
    raise ValueError("`vars_to_warm_start must be a `list` or `str`.  Given "
                     "type is {}".format(type(vars_to_warm_start)))
# We have to deal with partitioned variables, since get_collection flattens
# out the list.
grouped_variables = {}
for v in list_of_vars:
    t = [v] if not isinstance(v, list) else v
    var_name = _infer_var_name(t)
    grouped_variables.setdefault(var_name, []).append(v)

exit(grouped_variables)
