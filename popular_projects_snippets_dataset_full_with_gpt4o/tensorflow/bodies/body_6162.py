# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Validate that given synchronization value is valid."""
synchronization = kwargs.get("synchronization",
                             vs.VariableSynchronization.AUTO)
if synchronization == vs.VariableSynchronization.NONE:
    raise ValueError(
        "`NONE` variable synchronization mode is not supported with "
        "tf.distribute strategy. Please change the `synchronization` for "
        "variable: " + str(kwargs["name"]))
if synchronization not in (vs.VariableSynchronization.ON_READ,
                           vs.VariableSynchronization.ON_WRITE,
                           vs.VariableSynchronization.AUTO):
    raise ValueError(
        "Invalid variable synchronization mode: %s for variable: %s" %
        (synchronization, kwargs["name"]))
if synchronization == vs.VariableSynchronization.AUTO:
    exit(vs.VariableSynchronization.ON_WRITE)
exit(synchronization)
