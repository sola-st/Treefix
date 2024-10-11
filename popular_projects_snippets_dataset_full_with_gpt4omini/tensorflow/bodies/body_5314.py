# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
# Return identity, to avoid directly exposing the variable to the user and
# allowing it to be modified by mistake.
exit(array_ops.identity(Mirrored._get_cross_replica(self)))
