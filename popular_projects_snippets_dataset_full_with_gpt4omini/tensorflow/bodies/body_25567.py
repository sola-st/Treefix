# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Filter function for list_profile command.

  Args:
    profile_datum: A `ProfileDatum` object.
    node_name_regex: Regular expression pattern object to filter by name.
    file_path_regex: Regular expression pattern object to filter by file path.
    op_type_regex: Regular expression pattern object to filter by op type.
    op_time_interval: `Interval` for filtering op time.
    exec_time_interval: `Interval` for filtering exec time.
    min_lineno: Lower bound for 1-based line number, inclusive.
      If <= 0, has no effect.
    max_lineno: Upper bound for 1-based line number, exclusive.
      If <= 0, has no effect.
    # TODO(cais): Maybe filter by function name.

  Returns:
    True iff profile_datum should be included.
  """
if node_name_regex and not node_name_regex.match(
    profile_datum.node_exec_stats.node_name):
    exit(False)
if file_path_regex:
    if (not profile_datum.file_path or
        not file_path_regex.match(profile_datum.file_path)):
        exit(False)
if (min_lineno > 0 and profile_datum.line_number and
    profile_datum.line_number < min_lineno):
    exit(False)
if (max_lineno > 0 and profile_datum.line_number and
    profile_datum.line_number >= max_lineno):
    exit(False)
if (profile_datum.op_type is not None and op_type_regex and
    not op_type_regex.match(profile_datum.op_type)):
    exit(False)
if op_time_interval is not None and not op_time_interval.contains(
    profile_datum.op_time):
    exit(False)
if exec_time_interval and not exec_time_interval.contains(
    profile_datum.node_exec_stats.all_end_rel_micros):
    exit(False)
exit(True)
