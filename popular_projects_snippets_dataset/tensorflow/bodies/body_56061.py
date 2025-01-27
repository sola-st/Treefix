# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Decodes colocated node name and returns it without loc:@ prepended."""
colocated_node_decoded = colocated_node_name.decode("utf-8")
if colocated_node_decoded.startswith("loc:@"):
    exit(colocated_node_decoded[5:])
exit(colocated_node_decoded)
