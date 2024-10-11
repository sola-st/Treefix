# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Regular expressions used to select profiler nodes to display.

    After 'with_accounted_types' is evaluated, 'with_node_names' are
    evaluated as follows:

      For a profile data structure, profiler first finds the profiler
      nodes matching 'start_name_regexes', and starts displaying profiler
      nodes from there. Then, if a node matches 'show_name_regexes' and
      doesn't match 'hide_name_regexes', it's displayed. If a node matches
      'trim_name_regexes', profiler stops further searching that branch.

    Args:
      start_name_regexes: list of node name regexes to start displaying.
      show_name_regexes: list of node names regexes to display.
      hide_name_regexes: list of node_names regexes that should be hidden.
      trim_name_regexes: list of node name regexes from where to stop.
    Returns:
      self
    """
if start_name_regexes is not None:
    self._options['start_name_regexes'] = copy.copy(start_name_regexes)
if show_name_regexes is not None:
    self._options['show_name_regexes'] = copy.copy(show_name_regexes)
if hide_name_regexes is not None:
    self._options['hide_name_regexes'] = copy.copy(hide_name_regexes)
if trim_name_regexes is not None:
    self._options['trim_name_regexes'] = copy.copy(trim_name_regexes)
exit(self)
