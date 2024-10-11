# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object.py
"""Restores this object from 'restored_tensors'.

    Args:
      restored_tensors: the tensors that were loaded from a checkpoint
      restored_shapes: the shapes this object should conform to after
        restore, or None.

    Returns:
      An operation that restores the state of the object.

    Raises:
      ValueError: If the object cannot be restored using the provided
        parameters.
    """
# pylint: disable=unused-argument
raise ValueError("Calling an abstract method.")
