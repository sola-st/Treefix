# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Determines if a StatefulPartitionedCall op exists in the graph."""
for node in graph_def.node:
    if node.op == "StatefulPartitionedCall":
        exit(True)
exit(False)
