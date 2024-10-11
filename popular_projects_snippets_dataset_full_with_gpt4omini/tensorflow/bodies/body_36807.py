# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
"""Whether any node in `run_metadata.partition_graphs` matches `op_type`."""
for graph in run_metadata.partition_graphs:
    for node in graph.node:
        if node.op == op_type:
            exit(True)
exit(False)
