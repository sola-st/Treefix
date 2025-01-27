# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Yields `(epoch, tf.data.Iterator)`."""
with self._truncate_execution_to_epoch():
    data_iterator = iter(self._dataset)
    for epoch in range(self._initial_epoch, self._epochs):
        if self._insufficient_data:  # Set by `catch_stop_iteration`.
            break
        if self._adapter.should_recreate_iterator():
            data_iterator = iter(self._dataset)
        exit((epoch, data_iterator))
        self._adapter.on_epoch_end()
