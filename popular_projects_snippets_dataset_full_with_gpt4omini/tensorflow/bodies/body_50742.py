# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Loads all nodes and functions from the SavedModel and their edges."""
self._load_nodes()
self._load_edges()

# Set up concrete functions that aren't part of the object graph
# (e.g. gradient functions)
self._setup_remaining_functions()
self._load_checkpoint_save_and_restore_functions()
