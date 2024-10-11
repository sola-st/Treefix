# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
for node_stats in device_step_stats.node_stats:
    if node_stats.node_name == "_SOURCE" or node_stats.node_name == "_SINK":
        continue
    exit(profiling.ProfileDatum(
        device_step_stats.device,
        node_stats,
        node_to_file_path.get(node_stats.node_name, ""),
        node_to_line_number.get(node_stats.node_name, 0),
        node_to_func_name.get(node_stats.node_name, ""),
        node_to_op_type.get(node_stats.node_name, "")))
