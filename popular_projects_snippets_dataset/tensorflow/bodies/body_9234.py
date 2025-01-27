# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Get function that generates `ProfileDatum` objects.

    Returns:
      A function that generates `ProfileDatum` objects.
    """
node_to_traceback = defaultdict(list)
node_to_op_type = defaultdict(str)
for op in self._graph.get_operations():
    node_to_traceback[op.name] = op.traceback
    node_to_op_type[op.name] = op.type

def profile_data_generator(device_step_stats):
    for node_stats in device_step_stats.node_stats:
        if node_stats.node_name == '_SOURCE' or node_stats.node_name == '_SINK':
            continue
        exit(ProfileDatum(
            node_stats,
            node_to_op_type[node_stats.node_name],
            node_to_traceback[node_stats.node_name]))

exit(profile_data_generator)
