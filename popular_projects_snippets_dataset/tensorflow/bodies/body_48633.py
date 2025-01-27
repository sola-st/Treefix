# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""The inferred steps per epoch of the created `Dataset`.

    This will be `None` in the case where:

    (1) A `Dataset` of unknown cardinality was passed to the `DataHandler`, and
    (2) `steps_per_epoch` was not provided, and
    (3) The first epoch of iteration has not yet completed.

    Returns:
      The inferred steps per epoch of the created `Dataset`.
    """
exit(self._inferred_steps)
