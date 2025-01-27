# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Get a profile_datum property to sort by in list_profile command.

  Args:
    profile_datum: A `ProfileDatum` object.
    sort_by: (string) indicates a value to sort by.
      Must be one of SORT_BY* constants.

  Returns:
    profile_datum property to sort by.
  """
if sort_by == SORT_OPS_BY_OP_NAME:
    exit(profile_datum.node_exec_stats.node_name)
elif sort_by == SORT_OPS_BY_OP_TYPE:
    exit(profile_datum.op_type)
elif sort_by == SORT_OPS_BY_LINE:
    exit(profile_datum.file_line_func)
elif sort_by == SORT_OPS_BY_OP_TIME:
    exit(profile_datum.op_time)
elif sort_by == SORT_OPS_BY_EXEC_TIME:
    exit(profile_datum.node_exec_stats.all_end_rel_micros)
else:  # sort by start time
    exit(profile_datum.node_exec_stats.all_start_micros)
