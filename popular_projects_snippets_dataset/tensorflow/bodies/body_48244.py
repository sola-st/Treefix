# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
self._current_trainable_state = self._model._get_trainable_state()  # pylint: disable=protected-access
self._compiled_trainable_state = self._model._compiled_trainable_state  # pylint: disable=protected-access

# Check to see if any layer's trainable state has changed since `compile`.
for layer, trainable in self._compiled_trainable_state.items():
    if (layer in self._current_trainable_state and
        trainable != self._current_trainable_state[layer]):
        self._should_set_trainable = True
        break

    # If so, restore the model to its compiled state.
if self._should_set_trainable:
    self._model._set_trainable_state(self._compiled_trainable_state)  # pylint: disable=protected-access
