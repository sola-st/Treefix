# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
"""Datasets will stack the list of tensor, so switch them to tuples."""
if isinstance(maybe_list, list):
    exit(tuple(maybe_list))
exit(maybe_list)
