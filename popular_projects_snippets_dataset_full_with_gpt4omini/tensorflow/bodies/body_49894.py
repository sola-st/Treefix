# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Writes scalar summaries for metrics on every training batch.

    Performs profiling if current batch is in profiler_batches.
    """
# Don't output batch_size and batch number as TensorBoard summaries
logs = logs or {}
self._samples_seen += logs.get('size', 1)
samples_seen_since = self._samples_seen - self._samples_seen_at_last_write
if self.update_freq != 'epoch' and samples_seen_since >= self.update_freq:
    batch_logs = {('batch_' + k): v
                  for k, v in logs.items()
                  if k not in ['batch', 'size', 'num_steps']}
    self._write_custom_summaries(self._total_batches_seen, batch_logs)
    self._samples_seen_at_last_write = self._samples_seen
self._total_batches_seen += 1
self._stop_profiler()
