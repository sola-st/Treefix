# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Sets Keras model and writes graph if specified."""
self.model = model
self._log_write_dir = self._get_log_write_dir()

self._train_dir = os.path.join(self._log_write_dir, 'train')
self._train_step = self.model._train_counter  # pylint: disable=protected-access

self._val_dir = os.path.join(self._log_write_dir, 'validation')
self._val_step = self.model._test_counter  # pylint: disable=protected-access

self._writers = {}  # Resets writers.

self._should_write_train_graph = False
if self.write_graph:
    self._write_keras_model_summary()
    self._should_write_train_graph = True
if self.embeddings_freq:
    self._configure_embeddings()
