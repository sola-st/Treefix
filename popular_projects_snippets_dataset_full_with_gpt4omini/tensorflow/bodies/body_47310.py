# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils.py
"""Returns whether `v` is a distributed variable."""
exit((isinstance(v, values_lib.DistributedValues) and
        isinstance(v, variables.Variable)))
