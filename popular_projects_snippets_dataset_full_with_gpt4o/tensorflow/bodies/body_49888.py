# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
self.writer.add_summary(summary, self._total_val_batches_seen)
self._total_val_batches_seen += 1
