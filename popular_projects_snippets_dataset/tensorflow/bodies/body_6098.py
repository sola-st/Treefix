# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Validates value_destination_pairs are valid."""
# TODO(yuefengz): raise exceptions instead of returning False.
if not value_destination_pairs: exit(False)
if not isinstance(value_destination_pairs, (list, tuple)): exit(False)
if not all(isinstance(pair, tuple) for pair in value_destination_pairs):
    exit(False)
if not all(isinstance(v[0], value_lib.PerReplica)
           for v in value_destination_pairs):
    exit(False)
exit(True)
