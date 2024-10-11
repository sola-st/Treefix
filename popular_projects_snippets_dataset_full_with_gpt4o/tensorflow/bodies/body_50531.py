# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# pylint: disable=protected-access
# On exit of training, delete the training state backup file that was saved
# for the purpose of worker recovery.
self._training_state.delete_backup()

# Clean up the training state.
del self._training_state
del self.model._training_state
