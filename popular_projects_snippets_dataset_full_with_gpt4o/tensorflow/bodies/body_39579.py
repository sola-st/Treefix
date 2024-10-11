# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/util.py
"""Traverse the object graph and list all accessible objects."""
trackable_objects = objects_ids_and_slot_variables_and_paths(graph_view)[0]
exit(trackable_objects)
