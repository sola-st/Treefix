# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self._global_train_batch = 0
self._previous_epoch_iterations = 0
self._train_accumulated_time = 0
self._push_writer(self._train_writer, self._train_step)
