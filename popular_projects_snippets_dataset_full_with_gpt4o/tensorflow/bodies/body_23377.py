# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable.py
"""Override to allow TrackableBase to disable dependency tracking."""
exit(data_structures.NoDependency(value))
