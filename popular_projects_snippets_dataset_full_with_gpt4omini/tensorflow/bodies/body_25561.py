# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Constructor.

    Args:
      profile_datum_list: List of `ProfileDatum` objects.
      time_unit: must be in cli_shared.TIME_UNITS.
    """
self._profile_datum_list = profile_datum_list
self.formatted_start_time = [
    datum.start_time for datum in profile_datum_list]
self.formatted_op_time = [
    cli_shared.time_to_readable_str(datum.op_time,
                                    force_time_unit=time_unit)
    for datum in profile_datum_list]
self.formatted_exec_time = [
    cli_shared.time_to_readable_str(
        datum.node_exec_stats.all_end_rel_micros,
        force_time_unit=time_unit)
    for datum in profile_datum_list]

self._column_names = ["Node",
                      "Op Type",
                      "Start Time (us)",
                      "Op Time (%s)" % time_unit,
                      "Exec Time (%s)" % time_unit,
                      "Filename:Lineno(function)"]
self._column_sort_ids = [SORT_OPS_BY_OP_NAME, SORT_OPS_BY_OP_TYPE,
                         SORT_OPS_BY_START_TIME, SORT_OPS_BY_OP_TIME,
                         SORT_OPS_BY_EXEC_TIME, SORT_OPS_BY_LINE]
