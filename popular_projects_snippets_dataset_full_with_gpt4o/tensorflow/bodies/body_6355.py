# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Return 0 instead of a constant tensor to avoid creating a new node for
# users who don't use distribution strategy.
exit(0)
