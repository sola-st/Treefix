# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
# If we set the values to their compiled state in __enter__, we need to
# restore the original values before leaving the scope.
if self._should_set_trainable:
    self._model._set_trainable_state(self._current_trainable_state)  # pylint: disable=protected-access
exit(False)  # False values do not suppress exceptions
