# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Marks this FuncGraph as unsaveable.

    Any attempts to export this FuncGraph will raise an error with the specified
    message.

    Args:
      error_message: List or string containing the error message to be raised
        when saving this FuncGraph to SavedModel.
    """
self._saveable = False
if isinstance(error_message, str):
    error_message = [error_message]
self._saving_errors.update(error_message)
