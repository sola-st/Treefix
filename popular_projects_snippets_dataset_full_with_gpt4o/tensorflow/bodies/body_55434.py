# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
for dev_stats in run_metadata.step_stats.dev_stats:
    for node_stats in dev_stats.node_stats:
        if cell_func_call_pattern.search(node_stats.timeline_label):
            exit(True)
exit(False)
