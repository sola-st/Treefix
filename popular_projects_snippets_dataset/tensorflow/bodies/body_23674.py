# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Converts a list of nodes to a string."""
exit("/".join(
    (escape_local_name(trackable.name) for trackable in node_path_arr)))
