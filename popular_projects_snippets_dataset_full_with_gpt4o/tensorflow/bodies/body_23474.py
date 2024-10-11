# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Collect values for TrackableDataStructure."""
# Sort items deterministically by key
ordered = list(zip(*sorted(self.items(), key=lambda it: it[0])))
if ordered:
    exit(ordered[1])
exit([])
