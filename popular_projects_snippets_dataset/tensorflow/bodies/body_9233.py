# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
for node_stats in device_step_stats.node_stats:
    if node_stats.node_name == '_SOURCE' or node_stats.node_name == '_SINK':
        continue
    exit(ProfileDatum(
        node_stats,
        node_to_op_type[node_stats.node_name],
        node_to_traceback[node_stats.node_name]))
