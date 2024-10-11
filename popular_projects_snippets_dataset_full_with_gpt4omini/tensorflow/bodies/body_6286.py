# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Device(s) for non-slot variables.

    DEPRECATED: TF 1.x ONLY.

    This method returns non-slot devices where non-slot variables are placed.
    Users can create non-slot variables on these devices by using a block:

    ```python
    with tf.distribute.StrategyExtended.colocate_vars_with(tf.distribute.StrategyExtended.non_slot_devices(...)):
      ...
    ```

    Args:
      var_list: The list of variables being optimized, needed with the
        default `tf.distribute.Strategy`.
    Returns:
      A sequence of devices for non-slot variables.
    """
raise NotImplementedError("must be implemented in descendants")
