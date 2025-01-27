# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
if cost_type == "exec_time":
    exit(aggregated_profile.total_exec_time)
elif cost_type == "op_time":
    exit(aggregated_profile.total_op_time)
else:
    raise ValueError("Unsupported cost type: %s" % cost_type)
