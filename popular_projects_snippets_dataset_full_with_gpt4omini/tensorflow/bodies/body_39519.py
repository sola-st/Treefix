# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Add a variable to the list of optionally restored variables.

    There are situations where certain variables should be ignored in assertions
    such as assert_existing_objects_matched(). One example is that of a
    checkpoint saved with train.Saver(), and restored with train.Checkpoint():
    it is possible for the train.Saver() checkpoint to be missing the internal
    `save_counter` variable, which we want to ignore on restore.

    Args:
      var: The variable to treat as optionally restored.
    """
self._optionally_restored.append(var)
