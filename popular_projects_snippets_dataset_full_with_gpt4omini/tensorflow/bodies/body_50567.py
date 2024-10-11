# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Runs metrics and histogram summaries at epoch end."""
self._log_epoch_metrics(epoch, logs)

if self.histogram_freq and epoch % self.histogram_freq == 0:
    self._log_weights(epoch)

if self.embeddings_freq and epoch % self.embeddings_freq == 0:
    self._log_embeddings(epoch)
