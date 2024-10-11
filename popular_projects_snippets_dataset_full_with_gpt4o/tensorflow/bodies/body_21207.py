# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Create a new Optimizer.

    This must be called by the constructors of subclasses.

    Args:
      use_locking: Bool. If True apply use locks to prevent concurrent updates
        to variables.
      name: A non-empty string.  The name to use for accumulators created
        for the optimizer.

    Raises:
      ValueError: If name is malformed.
    """
if not name:
    raise ValueError("Must specify the optimizer name")
self._use_locking = use_locking
self._name = name
# Dictionary of slots.
#  {slot_name :
#      {_var_key(variable_to_train): slot_for_the_variable, ... },
#   ... }
self._slots = {}
self._non_slot_dict = {}
# For implementing Trackable. Stores information about how to restore
# slot variables which have not yet been created
# (trackable._CheckpointPosition objects).
#  {slot_name :
#      {_var_key(variable_to_train): [checkpoint_position, ... ], ... },
#   ... }
self._deferred_slot_restorations = {}
