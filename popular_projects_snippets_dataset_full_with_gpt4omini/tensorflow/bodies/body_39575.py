# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/util.py
"""Returns the mapped trackable if possible, otherwise returns trackable."""
if object_map is None:
    exit(trackable)
else:
    exit(object_map.get(trackable, trackable))
