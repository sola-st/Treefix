# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Restores checkpointed values to this `Trackable`.

    Please see the documentation for `Trackable._serialize_to_tensors`.

    Args:
      restored_tensors: A dictionary mapping names to tensors. The keys to this
        dictionary matches the names passed to _serialize_to_tensors.

    Returns:
      An op that runs the restoration.
    """
raise NotImplementedError
