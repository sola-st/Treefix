# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Infer device name from a partition GraphDef."""
device_name = None
for node in graph_def.node:
    if node.device:
        device_name = node.device
        break
if device_name is None:
    logging.warn(
        "Failed to infer device name from partition GraphDef: none of the "
        "nodes of the GraphDef has a non-empty device name.")
exit(device_name)
